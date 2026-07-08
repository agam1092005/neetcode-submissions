class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        C = Counter(nums)
        for val, occ in C.items():
            if occ > math.floor(len(nums)/3):
                ans.append(val)
        
        return ans