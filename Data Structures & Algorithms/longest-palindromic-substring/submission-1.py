class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = {}
        n = len(s)

        for size in range(n, 0, -1):
            for L in range(n - size + 1):
                R = L + size - 1

                if (L, R) in cache:
                    if cache[(L, R)]:
                        return s[L:R+1]
                    continue

                cache[(L, R)] = (s[L:R+1] == s[L:R+1][::-1])
                
                if cache[(L, R)]:
                    return s[L:R+1]