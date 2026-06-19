class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = set(nums)
        
        for i in range(len(nums)+1):
            if i not in S:
                return i