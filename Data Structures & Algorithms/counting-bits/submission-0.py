class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            curr = 0
            while i:
                curr += i % 2
                i = i >> 1
            ans.append(curr)

        return ans