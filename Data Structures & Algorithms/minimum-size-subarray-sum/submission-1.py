class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        if (max(nums) >= target):
            return 1
        
        ans = float("inf")
        L = 0
        total = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                ans = min(R-L+1, ans)
                total -= nums[L]
                L += 1

        return 0 if ans == float("inf") else ans