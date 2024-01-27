from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.q = deque()

        self.key_valTime = dict()
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.key_valTime:
            self.key_valTime[key] = (self.key_valTime[key][0], self.time)
            self.q.append((key, self.time))
            return self.key_valTime[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        self.q.append((key, self.time))
        if key in self.key_valTime:
            self.key_valTime[key] = (value, self.time)
            return

        if len(self.key_valTime) < self.cap:
            self.key_valTime[key] = (value, self.time)
        else:
            while True:
                cur_key, cur_time = self.q.popleft()
                if self.key_valTime[cur_key][1] != cur_time:
                    continue
                del self.key_valTime[cur_key]
                self.key_valTime[key] = (value, self.time)
                break
                 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)