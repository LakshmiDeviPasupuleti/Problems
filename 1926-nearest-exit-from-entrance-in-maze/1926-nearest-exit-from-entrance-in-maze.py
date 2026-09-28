class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m=len(maze)
        n=len(maze[0])
        queue=deque()
        queue.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]]='+'
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        while queue :
            row,col,step=queue.popleft()
            for dr,dc in directions :
                nr=dr+row
                nc=dc+col
                if 0<=nr<m and 0<=nc<n:
                    if maze[nr][nc]==".":
                        if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                            return step+1
                        maze[nr][nc]="+"
                        queue.append((nr,nc,step+1))

        return -1