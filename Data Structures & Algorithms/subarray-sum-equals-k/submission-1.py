class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, curr = 0, 0
        prefix = {0:1}
        for i in nums:
            curr += i
            diff = curr - k

            ans += prefix.get(diff, 0)
            prefix[curr] = 1 + prefix.get(curr, 0)
        
        return ans