#!/usr/bin/env python3
"""
Defines the MRUCache class
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Defines a MRU caching system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializes the MRUCache class
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
            mru_key = self.keys.pop()
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]
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
