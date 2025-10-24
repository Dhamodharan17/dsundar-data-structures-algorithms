from collections import deque
class Solution:
    # Sweeper
    def bfs(self, adj):
        
        q = deque([0])
        visited = set()
        visited.add(0)
        result = list()
        
        while q:
            curNode = q.popleft()
            result.append(curNode)
            # visited branches
            for b in adj[curNode]:
                if b not in visited:
                    visited.add(b)
                    q.append(b)
                    
        return result
