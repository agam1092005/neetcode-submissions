class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n

        def dfs(node):
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1

        return count
