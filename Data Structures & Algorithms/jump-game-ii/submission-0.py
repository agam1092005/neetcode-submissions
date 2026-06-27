class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        L, R = 0, 0

        while R < len(nums)-1:
            curr = 0
            for i in range(L, R+1):
                curr = max(curr, i + nums[i])
            L = R + 1
            R = curr
            ans += 1
        return ans