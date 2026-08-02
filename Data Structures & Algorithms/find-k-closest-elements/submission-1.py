class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = []

        for i in arr:
            L.append((i, abs(i-x)))

        ans = []

        for num, dist in sorted(L, key=lambda item: (item[1], item[0])):
            if k:
                ans.append(num)
                k -= 1

        return sorted(ans)