class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) 
        dp = [[0] * (amount+1) for _ in range(n+1)] 

        for i in range(n+1): 
            dp[i][0] = 1 
        
        for i in range(1, n+1) : 
            c = coins[i-1] 
            for j in range(1, amount +1): 
                dp[i][j] = dp[i-1][j] 
                if j >= c: 
                    dp[i][j] += dp[i][j-c] 

        return dp[n][amount]

