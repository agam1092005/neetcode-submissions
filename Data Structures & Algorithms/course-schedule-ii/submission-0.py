class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finished = 0
        ans = []
        while q:
            node = q.popleft()
            finished += 1
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    q.append(neighbour)

        if (finished != numCourses):
            return []
        return ans[::-1]
        
