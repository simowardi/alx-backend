#!/usr/bin/env python3
"""
Defines the LIFOCache class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines a LIFO caching system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializes the LIFOCache class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.keys.pop()
            print("DISCARD:", last_key)
            del self.cache_data[last_key]
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
