class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(rem):
            if rem == 0:
                return 0
                
            if rem < 0:
                return float("inf")

            if rem in cache:
                return cache[rem]

            ans = float("inf")

            for coin in coins:
                ans = min(ans, 1 + dfs(rem - coin))

            cache[rem] = ans
            return ans

        res = dfs(amount)
        return -1 if res == float("inf") else res