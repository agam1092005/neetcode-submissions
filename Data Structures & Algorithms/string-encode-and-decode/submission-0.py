class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += f"{len(i)}"
            ans += '^'
            ans += i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '^':
                j += 1
            
            l = int(s[i:j])
            j += 1
            ans.append(s[j:j+l])
            i = j+l

        return ans
