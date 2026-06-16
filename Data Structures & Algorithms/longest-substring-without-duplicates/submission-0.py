class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        window = 0
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[window])
                    window += 1
                    
            seen.add(s[i])
            maxi = max(maxi, i-window+1)
        return maxi
