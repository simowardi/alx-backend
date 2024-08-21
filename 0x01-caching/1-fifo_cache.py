#!/usr/bin/env python3
"""
Defines the FIFOCache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a FIFO caching system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializes the FIFOCache class
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
