class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * (n+1) for _ in range(m+1)] 
        for i in range(m+1): 
            dp[i][0] = 1 
        for i in range(n+1): 
            dp[0][i] = 1 

        for r in range(0, m): 
            for c in range(0, n): 
                down = dp[r+1][c]
                right = dp[r][c+1]

                dp[r+1][c+1] = down + right

        return dp[r][c]

