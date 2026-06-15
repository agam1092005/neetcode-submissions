class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        ans = 1
        L = set(nums)

        for i in nums:
            if i-1 not in L:
                curr = 1
                while (i+curr) in L:
                    curr += 1
                ans = max(ans, curr)
    
        return ans