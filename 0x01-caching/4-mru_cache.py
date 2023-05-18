#!/usr/bin/env python3
""" MRU Caching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class
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
            most_recent_key = self.usage_tracker.pop()
            print(f"DISCARD: {most_recent_key}")
            del self.cache_data[most_recent_key]

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
