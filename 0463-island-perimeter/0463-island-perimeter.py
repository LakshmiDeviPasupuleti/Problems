class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        prem=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:
                        prem +=1
                    if i==m-1 or grid[i+1][j]==0:
                        prem +=1
                    if j==0 or grid[i][j-1]==0:
                        prem +=1
                    if j==n-1 or grid[i][j+1]==0:
                        prem +=1
        return prem
        