class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def palindrome(x):
            return x == x[::-1]

        def dfs(i, curr):
            if i == len(s):
                ans.append(curr.copy())
                return

            for j in range(i, len(s)):
                part = s[i:j+1]
                if palindrome(part):
                    curr.append(part)
                    dfs(j+1, curr)
                    curr.pop()

        dfs(0, [])
        return ans