"""
design DS that follows LRU cache constraint
(1) LRU cache is initialized with positive size capacity
(2) get(key:int): return val if keys exists, else return -1
(3) put(key:int, value:int): update value of key if it exists, else add key value pair to cache
    if # of keys makes cache exceed capacity, evict recently used key
Must run in O(1) avg capacity
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = []
        self.cache = {}

    def get(self, key: int) -> int:
        LRU = self.cache
        if key in LRU:
            return LRU[key]
        return -1

    def put(self, key: int, value: int) -> None:
        LRU = self.cache
        store = self.store
        if key in LRU:
            LRU[key] = value
            store.append(key)
        else:
            if len(store) == self.capacity:
                last_key = store.pop()
                del LRU[last_key]
                store.append(key)
                LRU[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Actual solution
"""
