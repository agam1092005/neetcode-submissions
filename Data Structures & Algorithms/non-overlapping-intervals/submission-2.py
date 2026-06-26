class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0])
        last = intervals[0][1]

        for i in intervals[1:]:

            if i[0] >= last:
                last = i[1]
            else:
                count += 1
                last = min(last, i[1])

        return count