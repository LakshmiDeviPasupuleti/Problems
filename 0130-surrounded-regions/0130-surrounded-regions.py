
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if board[i][j] != 'O':
                return

            # Mark safe O as visited
            board[i][j] = '#'

            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right

        # Check first and last rows
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)

            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        # Check first and last columns
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)

            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        # Capture surrounded O cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
