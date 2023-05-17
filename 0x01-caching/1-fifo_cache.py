#!/usr/bin/env python3
""" FIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching
    """
    def __init__(self):
        """Init method
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keys_order.append(key)

            if len(self.keys_order) > BaseCaching.MAX_ITEMS:
                oldest_key = self.keys_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Get method
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
