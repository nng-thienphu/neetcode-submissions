class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n+1)

        def dp(i): 
            if i <= 1 : 
                return 0 
            if memo[i] != -1: 
                return memo[i]

            step1 = dp(i-1) + cost[i-1] 
            step2 = dp(i-2) + cost[i-2] 
            memo[i] = min(step1, step2) 
            return memo[i]
        
        return dp(n) 
