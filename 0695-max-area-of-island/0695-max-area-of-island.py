class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_area=0
        def dfs(r,c):
            if r < 0 or r >= m or c<0 or c>=n:
                return 0
            if grid[r][c]==0:
                return 0
            grid[r][c]=0
            area=1
            area +=dfs(r-1,c)
            area +=dfs(r+1,c)
            area +=dfs(r,c+1)
            area +=dfs(r,c-1)
            return area
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    max_area=max(max_area,area)
        return max_area
