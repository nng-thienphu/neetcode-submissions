class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. define the state dp + base case
        n = len(cost)
        dp = [0] * (n+1) # n stairs + 1 step to the roof top 
        dp[0] = 0
        dp[1] = 0
        
        # 2. fill order
        for i in range(2, n+1): 
            dp[i] =   min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]) 

        return dp[n]   