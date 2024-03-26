#!/usr/bin/env python3
"""
Writing strings to Redis
Cache class
"""

import uuid
from functools import wraps
from typing import Callable, Union

import redis


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
