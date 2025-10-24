class Solution:

    direct = [[0,1], [0,-1], [1,0], [-1,0]]
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # number of connected components
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.performDfs(i,j)
                    count += 1
        return count

    def performDfs(self, x,y):
        if x < 0 or y < 0 or x >= self.m or y >= self.n or self.grid[x][y] != '1':
            return
        self.grid[x][y] = 0
        for dx, dy in self.direct:
            nx, ny = x+dx, y+dy
            self.performDfs(nx, ny)



       



        
