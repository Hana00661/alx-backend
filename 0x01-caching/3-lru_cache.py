#!/usr/bin/env python3

"""3-lru_cache.py
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """a class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
