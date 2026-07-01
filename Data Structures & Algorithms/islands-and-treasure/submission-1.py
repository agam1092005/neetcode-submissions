class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        INF = 2147483647
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit):
                return INF
            
            if grid[r][c] == 0:
                return 0

            visit.add((r, c))
            distance = INF
            for dr, dc in directions:
                distance = min(distance, 1 + dfs(r + dr, c + dc))
            visit.remove((r, c))
            
            return distance

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)        
