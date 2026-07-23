class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1) 
        dp[0] = 0

        for i in range(1, n+1): 
            for s in range(1, i): 
                remain = i - s** 2
                if remain < 0: 
                    break
                dp[i] = min(dp[i], 1 + dp[remain]) 
        
        return dp[n]
        yeah 