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
        self.keys_order = []

    def put(self, key, item):
        """ Put method """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keys_order.append(key)

            if len(self.keys_order) > BaseCaching.MAX_ITEMS:
                last_key = self.keys_order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ get method """
        if key is not None:
            return self.cache_data.get(key)
        return None
