class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(remaining): 
            if remaining == 0: 
                return 1
            if remaining < 0: 
                return 0
            
            if remaining in memo: 
                return memo[remaining]
            
            memo[remaining] = dp(remaining - 1) + dp(remaining - 2)
            
            return memo[remaining]
        
        return dp(n)
