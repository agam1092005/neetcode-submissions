class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mini = 0
        maxi = max(nums)+1

        while mini != maxi or mini < 1:
            mini += 1
            if mini not in nums and mini > 0:
                return mini