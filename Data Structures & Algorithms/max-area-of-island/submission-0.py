class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()

        ans = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            curr = 1
            for dr, dc in directions:
                curr += dfs(r + dr, c + dc)
            
            return curr
        

        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c))

        return ans