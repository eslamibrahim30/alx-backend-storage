#!/usr/bin/env python3
"""
This module for task "Writing strings to Redis"
"""
import redis
import uuid
from typing import Union


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
