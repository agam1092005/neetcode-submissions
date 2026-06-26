class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        ans  = []
        start = newInterval[0]
        left, right = 0, len(intervals)-1

        while left <= right:
            mid = left + (right-left)//2

            if intervals[mid][0] < start:
                left = mid+1
            else:
                right = mid-1
            
        intervals.insert(left, newInterval)

        for i in intervals:
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
            
        return ans