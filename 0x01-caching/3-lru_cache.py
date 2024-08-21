#!/usr/bin/env python3
"""
Defines the LRUCache class
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines a LRU caching system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializes the LRUCache class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.keys.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
