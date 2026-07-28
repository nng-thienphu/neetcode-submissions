class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        inf = float("inf")
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[inf] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[0][1] = 0                       # sentinel: virtual entrance above (0,0)

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r - 1][c - 1]

        return dp[ROWS][COLS]