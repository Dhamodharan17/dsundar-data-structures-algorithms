# multi source bfs + flood fill
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def valid(x, y):
            # rotte only fresh
            return x<m and y<n and x>=0 and y>=0 
             and grid[x][y] == 1

        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        # add rotten oranges to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        #flood fill the rotten orange
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if valid(nx, ny):
                        q.append([nx, ny])
                        grid[nx][ny] += 1
                        fresh -= 1
            #atlast - last rotten orange have no one to rotte
            level += 1
        
        return -1 if fresh !=0 else level-1
