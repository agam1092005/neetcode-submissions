class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = []
        if not t or len(s) < len(t):
            return ""
        if s == t:
            return s

        L = 0
        for R in range(len(s)):
            curr = None
            if s[R] in t:
                arr = [*t]
                if len(s[R:]) >= len(t):
                    temp = s[R:]
                    i = 0
                    while arr and i < len(temp):
                        if temp[i] in arr:
                            arr.remove(temp[i])

                        if not arr:
                            curr = temp[0:i+1]
                            break
                        i += 1

            if curr != None:
                ans.append(curr)             

        return min(ans, key=len) if ans else ""
