class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()
        P = set()
        A = set()

        def dfs(r, c, visit, prev):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev or (r, c) in visit):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, P, heights[r][0])
            dfs(r, COLS - 1, A, heights[r][COLS - 1])
    
        for c in range(COLS):
            dfs(0, c, P, heights[0][c])
            dfs(ROWS - 1, c, A, heights[ROWS - 1][c])
        
        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in P and (r, c) in A:
                    ans.append([r, c])
        
        return ans