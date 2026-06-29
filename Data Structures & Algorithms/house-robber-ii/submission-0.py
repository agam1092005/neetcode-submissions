class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        cache = [-1] * n

        def dfs(i, end):
            if i > end:
                return 0
                
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i + 1, end), nums[i] + dfs(i + 2, end))
            return cache[i]

        ans1 = dfs(0, n - 2)

        cache = [-1] * n      
        ans2 = dfs(1, n - 1)

        return max(ans1, ans2)