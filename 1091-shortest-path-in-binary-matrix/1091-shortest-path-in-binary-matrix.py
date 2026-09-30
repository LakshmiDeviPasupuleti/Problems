class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1
        queue=deque()   
        queue.append((0, 0, 1))
        directions = [
            (-1, -1),  # ↖ top-left
            (-1,  0),  # ↑ top
            (-1,  1),  # ↗ top-right
            ( 0, -1),  # ← left
            ( 0,  1),  # → right
            ( 1, -1),  # ↙ bottom-left
            ( 1,  0),  # ↓ bottom
             (1,  1)   # ↘ bottom-right
        ]
        grid[0][0]=1
        while queue:
            r,c,count=queue.popleft()
            if r==m-1 and c==n-1:
                return count
            for dr,dc in directions :
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    queue.append((nr,nc,count+1))
        return -1