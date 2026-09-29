class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh +=1
        min=0
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i,j=queue.popleft()
                for di,dj in directions:
                    ni=i+di
                    nj=j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        fresh=fresh-1
                        queue.append((ni,nj))
            min +=1
        if fresh >0:
            return -1
        return min
