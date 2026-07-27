class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * (n) for _ in range(m)] 
        for i in range(m): 
            dp[i][0] = 1 
        for i in range(n): 
            dp[0][i] = 1 

        for r in range(1, m): 
            for c in range(1, n): 
                up = dp[r-1][c]
                left = dp[r][c-1]

                dp[r][c] = up + left

        return dp[m-1][n-1]