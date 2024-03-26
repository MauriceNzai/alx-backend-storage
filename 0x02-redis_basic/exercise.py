#!/usr/bin/env python3
"""
Writing strings to Redis
Cache class
"""

import uuid
from functools import wraps
from typing import Callable, Union

import redis


def count_calls(method: Callable) -> Callable:
    """
    counts how many times methods of the Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def  wrapper(self, *args, **kwargs):
        """
        lncreases count for the particular key on every call of that method
        """
        self._redis.incr(key)
        return  method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
     stores the history of inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        saves function input parameters to one list in redis,
        and store function output into another list.
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        output = method(self, *args, **kwargs)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper

def replay(fn: Callable) -> Callable:
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{f_name}(*{i}) -> {o}')


class Cache:
    """
    store an instance of the Redis client
    """
    def init(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method to store data to redis server
        Args:
            data: data to be stored, can be any of [str, bytes, int, float]
        Returns:
                str: string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,  key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """
         Reads data from Redis and reconverts it to its original python type
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        converts data from redis into a python str variable
        """
        var = self._redis.get(key)
        return var.decode("UTF-8")

    def get_int(self, key: str) -> int:
        """
         converts data from redis into a python int variable
        """
        var = self._redis.get(key)
        try:
            var = int(var.decode("UTF-8"))
        except Exception:
            var = 0
        return var
