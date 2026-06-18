class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        L, R = 1, max(piles)

        while L <= R:
            mid = L + (R-L)//2
            curr = sum([math.ceil(i/mid) for i in piles])
            if curr <= h:
                R = mid-1      
            else:
                L = mid+1      

        return L
                