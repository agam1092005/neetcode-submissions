class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        temp = abs(temp)
        ans = int(str(temp)[::-1])

        if x < 0:
            ans *= -1
        
        if not (-2**31 <= ans <= 2**31 - 1):
            return 0
        
        return ans
