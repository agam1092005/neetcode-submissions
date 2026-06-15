class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue
            
            L, R = idx+1, len(nums)-1
            while L < R:
                curr = val + nums[L] + nums[R]
                if curr > 0:
                    R -= 1
                elif curr < 0:
                    L += 1
                else:
                    ans.append([val, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L-1] and L < R:
                        L +=1

        return ans