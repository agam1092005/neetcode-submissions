from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.usage = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.usage.remove(key)
        self.usage.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.usage.remove(key)
            self.usage.append(key)
            return

        self.cache[key] = value
        self.usage.append(key)

        if len(self.cache) > self.capacity:
            # remove from usage and then cache
            lru = self.usage.popleft()
            self.cache.pop(lru)
