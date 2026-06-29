class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mini, maxi = 1, 1

        for i in nums:
            temp = maxi * i
            maxi = max(i * maxi, i * mini, i)
            mini = min(temp, i * mini, i)
            ans = max(ans, maxi)
        
        return ans