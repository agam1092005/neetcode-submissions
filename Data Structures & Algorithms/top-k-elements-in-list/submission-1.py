class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        seen = Counter(nums)
        count = [[] for _ in range(len(nums)+1)]
        
        for val, occ in seen.items():
            count[occ].append(val)

        ans = []
        
        for i in range(len(count)-1, 0, -1):
            for j in count[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans