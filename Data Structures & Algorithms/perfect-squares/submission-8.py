class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1] * (n+1) 
        dp[0] = 0

        for i in range(1, n+1): 
            for s in range(1, i+1):  # have to include i for example i = 1 => s = 1 as well 
                remain = i - s** 2
                if remain < 0:   # this equivalent to "for s in range(1, int(i ** 0.5) + 1)" 
                    break
                dp[i] = min(dp[i], 1 + dp[remain]) 
        
        return dp[n]
