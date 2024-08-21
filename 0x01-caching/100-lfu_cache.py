#!/usr/bin/env python3
"""
Defines the LFUCache class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Defines a LFU caching system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializes the LFUCache class
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = {}
        self.last_used = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least frequently used item
            # If there is a tie, discard the least recently used
            min_freq = float('inf')
            least_recently_used = None
            for k, v in self.frequency.items():
                if v < min_freq:
                    min_freq = v
                    least_recently_used = k
                elif v == min_freq and self.last_used[k] < self.last_used[least_recently_used]:
                    least_recently_used = k
            print("DISCARD:", least_recently_used)
            del self.cache_data[least_recently_used]
            del self.frequency[least_recently_used]
            del self.last_used[least_recently_used]

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.last_used[key] = len(self.last_used)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.last_used[key] = len(self.last_used)
        return self.cache_data[key]
