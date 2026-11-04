class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    heights[nr][nc] >= heights[r][c]):

                    dfs(nr, nc, visited)

        # Pacific: first row and first column
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: last row and last column
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Find common cells
        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result