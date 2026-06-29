class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in cache:
                return cache[i]

            # Take one digit
            ways = dfs(i + 1)

            # Take two digits
            if (i + 1) < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)

            cache[i] = ways
            return ways

        return dfs(0)