#!/usr/bin/env python3
""" LIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class
    """
    def __init__(self):
        """Init method
        """
        super().__init__()

    def put(self, key, item):
        """ put method
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[-2]
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]

    def get(self, key):
        """ get method
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
