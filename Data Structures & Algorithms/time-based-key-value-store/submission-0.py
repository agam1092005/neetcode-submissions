class TimeMap:

    def __init__(self):
        self.TimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, val = "", self.TimeMap.get(key, [])
        L, R = 0, len(val)-1
        
        while L <= R:
            mid = L + (R-L)//2
            if val[mid][1] <= timestamp:
                res = val[mid][0]
                L = mid+1
            else:
                R = mid-1
        
        return res
