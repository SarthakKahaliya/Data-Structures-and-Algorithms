from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cacheMap: 
            val = self.cacheMap[key]
            self.cacheMap.pop(key)
            self.cacheMap[key] = val
            return self.cacheMap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.cacheMap.pop(key)
        elif len(self.cacheMap) >= self.capacity:
            self.cacheMap.popitem(last=False)
        
        self.cacheMap[key] = value
        
        return
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)