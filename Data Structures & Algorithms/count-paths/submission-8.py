class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        out_of_bound = 0 
        base = 1 
        dp = [[0] * (n) for _ in range(m)] 
        for i in range(m): 
            dp[i][0] = 1 
        for i in range(n): 
            dp[0][i] = 1 

        for r in range(0, m-1): 
            for c in range(0, n-1): 
                down = dp[r+1][c]
                right = dp[r][c+1]

                dp[r+1][c+1] = down + right

        return dp[m-1][n-1]

