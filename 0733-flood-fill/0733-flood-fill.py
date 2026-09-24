class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original=image[sr][sc]
        if original == color :
            return image
        def dfs(r,c):
            image[r][c]=color
            directions=[
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
            ]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if ( 0<=nr < len(image) and 
                     0<=nc < len(image[0]) and
                     image[nr][nc]==original
                ):
                    dfs(nr,nc)
        dfs(sr,sc)
        return image