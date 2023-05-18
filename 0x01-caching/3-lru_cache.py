#!/usr/bin/env python3
""" LRU Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache Class
    """
    def __init__(self):
        super().__init__()
        self.usage_tracker = []

    def put(self, key, item):
        """ put method
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_tracker.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.usage_tracker.pop(0)
            print(f"DISCARD: {oldest_key}")
            del self.cache_data[oldest_key]

        self.cache_data[key] = item
        self.usage_tracker.append(key)

    def get(self, key):
        """ get method
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_tracker.remove(key)
        self.usage_tracker.append(key)
        return self.cache_data[key]
