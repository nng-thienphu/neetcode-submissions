class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        dp = [[0] * (capacity + 1) for _ in range(n+1)] 

        for i in range(1, n+1): 
            w = weight[i-1]
            p = profit[i-1]

            for j in range(1, capacity+1) : 
                dp[i][j] = dp[i-1][j]
                
                if j >= w: 
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + p) 
        
        return dp[n][capacity]