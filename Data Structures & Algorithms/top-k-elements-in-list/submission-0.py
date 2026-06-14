class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums)+1)]
        for i in set(nums):
            c = nums.count(i)
            count[c].append(i)

        ans = []
        
        for i in range(len(count)-1, 0, -1):
            for j in count[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans