class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. dp and base state 
        # KEY TRICK: dp element need to maxxing so that we can use the min later please
        dp = [amount+1] * (amount + 1)
        dp[0] = 0 

        # 2. fill in the table 
        for a in range(1, amount + 1): 
            for c in coins: 
                remain = a - c
                if remain >= 0: 
                    dp[a] = min(dp[a], 1 + dp[remain]) # 1 here represent the current coin
        
        return dp[amount] if dp[amount] != (amount +1) else -1

