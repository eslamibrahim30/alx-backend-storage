#!/usr/bin/env python3
"""
This module for task "Writing strings to Redis"
"""
import redis
import uuid
from typing import Union, Callable, Any


class Cache:
    """
    This class for creating an instance of cache using Redis.
    """
    def __init__(self):
        """
        This method initializes each attribute in a Cache object.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method stores the input data in Redis using random key.
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return str(key)

    def get(self, key: str, fn: Union[Callable, None]) -> Any:
        """
        This method returns data from redis.
        """
        data = self._redis.get(key)
        if data is None or fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        """
        This method returns string data from redis
        """
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """
        This method returns integer data from redis
        """
        return int(self._redis.get(key))
