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
