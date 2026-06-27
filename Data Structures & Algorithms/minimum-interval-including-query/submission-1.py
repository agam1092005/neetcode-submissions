class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        intervals.sort(key=lambda x: x[1]-x[0]+1)
                 
        for i in queries:
            to_add = -1
            for idx, val in enumerate(intervals):
                if (val[0] <= i <= val[1]):
                    to_add = (intervals[idx][1] - intervals[idx][0] + 1)
                    break
            ans.append(to_add)
                  
        return ans