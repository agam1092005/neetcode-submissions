class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        length, breadth = len(height), max(height)

        matrix = [[0] * length for _ in range(breadth)]
        temp = height[:]     
        for row in range(breadth):
            for col in range(length):
                if temp[col] > 0:
                    temp[col] -= 1
                    matrix[row][col] = 1

        for row in matrix:
            if 1 in row:
                ans += row[row.index(1):len(row)-row[::-1].index(1)].count(0)

        return ans