class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        S = Counter(list(s))
        T = Counter(list(t))
        return S == T