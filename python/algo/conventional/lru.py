#encoding=utf8
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self. cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None
        return value

    def set(self, key, value):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False) # True为stack,last为heap
            self.cache[key] = value

if __name__ ==  '__main__':
    c = LRUCache(5)
  
    for i in range(5,10):
        c.set(i,10*i)
      
      
    print c.cache, c.cache.keys()
      
    c.get(5)
    c.get(7)
      
    print c.cache, c.cache.keys()
      
    c.set(10,100)
    print c.cache, c.cache.keys()
      
    c.set(9,44)
    print c.cache, c.cache.keys()