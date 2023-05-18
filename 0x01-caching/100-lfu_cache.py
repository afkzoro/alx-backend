#!/usr/bin/env python3
""" LFU Caching """
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class
    """
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_tracker = []

    def put(self, key, item):
        """ put method
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_tracker.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            candidates = [k for k in self.frequency if
                          self.frequency[k] == min_frequency]
            least_recently_used = min(self.usage_tracker,
                                      key=self.usage_tracker.index)
            least_frequent_lru = min(candidates, key=self.frequency.get)
            print(f"DISCARD: {least_frequent_lru}")
            del self.cache_data[least_frequent_lru]
            self.usage_tracker.remove(least_frequent_lru)
            del self.frequency[least_frequent_lru]

        self.cache_data[key] = item
        self.usage_tracker.append(key)
        self.frequency[key] += 1

    def get(self, key):
        """ get method
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_tracker.remove(key)
        self.usage_tracker.append(key)
        self.frequency[key] += 1
        return self.cache_data[key]
