class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[M - 1][N - 1] == 1:
            return 0
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[1][1] = 1
        for r in range(1, M + 1):
            for c in range(1, N + 1):
                if grid[r - 1][c - 1] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r - 1][c]
                    dp[r][c] += dp[r][c - 1]
        return dp[M][N]