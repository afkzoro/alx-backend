#!/usr/bin/env python3
""" 0-base_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """ Put method
     """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get method
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
