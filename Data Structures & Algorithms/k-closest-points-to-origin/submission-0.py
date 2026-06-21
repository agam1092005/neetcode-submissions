import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            dis = (math.sqrt((0 - i[0])**2 + (0 - i[1])**2))
            heapq.heappush(heap, [dis, [i[0], i[1]]])

        heapq.heapify(heap)
        
        ans = []
        while k > 0:
            dis, i = heapq.heappop(heap)
            ans. append(i)
            k -= 1

        return ans