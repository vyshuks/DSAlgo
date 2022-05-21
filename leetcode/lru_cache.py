"""
https://leetcode.com/problems/lru-cache/
"""

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self._map = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self._map:
            value = self._map.pop(key)
            self._map[key] = value
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self._map.get(key):
            self._map.pop(key)
        elif len(self._map) == self.capacity:
            self._map.popitem(last=False)
        self._map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)