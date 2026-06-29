class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        cache = {}
        L = 0

        while L < len(s):
            R = L + 1
            while R <= len(s):
                word = s[L:R]
                if word in cache and cache[word]:
                    count += 1
                else:
                    if (word == word[::-1]):
                        count += 1
                    cache[word] = (word == word[::-1])

                R += 1
            L += 1
            
        return count