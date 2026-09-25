class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == 0:
                return

            grid[i][j] = 0

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # Boundary rows
        for j in range(n):

            if grid[0][j] == 1:
                dfs(0, j)

            if grid[m - 1][j] == 1:
                dfs(m - 1, j)

        # Boundary columns
        for i in range(m):

            if grid[i][0] == 1:
                dfs(i, 0)

            if grid[i][n - 1] == 1:
                dfs(i, n - 1)

        
        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    count += 1

        return count