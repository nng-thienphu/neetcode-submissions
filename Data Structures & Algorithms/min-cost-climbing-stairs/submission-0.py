class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}
        
        def dp(remaining):
            # Base case: reached the top
            if remaining <= 1:
                return 0
            
            # Check memo
            if remaining in memo:
                return memo[remaining]
            
            # Choice: take 1 step or 2 steps
            # Pay cost of the step you land on
            one_step = cost[remaining - 1] + dp(remaining - 1)
            two_step = cost[remaining - 2] + dp(remaining - 2)
            
            result = min(one_step, two_step)
            
            memo[remaining] = result
            return result
        
        return dp(n)