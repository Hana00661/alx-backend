#!/usr/bin/env python3
"""100-lfu_cache.py
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """a class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}
        self.last_used = {}
        self.count = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if self.count >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]
                if len(lfu_keys) > 1:
                    lru_key = min(self.last_used, key=self.last_used.get)
                    self.cache_data.pop(lru_key)
                    self.frequency.pop(lru_key)
                    self.last_used.pop(lru_key)
                else:
                    lfu_key = lfu_keys[0]
                    self.cache_data.pop(lfu_key)
                    self.frequency.pop(lfu_key)
                    self.last_used.pop(lfu_key)
                    self.count -= 1
                    print("DISCARD: {}".format(lfu_key))
            else:
                self.count += 1
            self.cache_data[key] = item
            self.frequency[key] = 1
        self.last_used[key] = self.count

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.last_used[key] = self.count
        return self.cache_data[key]
