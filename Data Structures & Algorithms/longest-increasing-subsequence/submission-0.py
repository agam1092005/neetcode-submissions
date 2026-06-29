class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if cache[i] != -1:
                return cache[i]
            
            curr = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    curr = max(curr, 1+dfs(j))
            
            cache[i] = curr
            return curr

        return max(dfs(i) for i in range(n))