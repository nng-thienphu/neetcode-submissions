class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. dp and base state
        dp = [0] * (amount + 1)
        dp[0] = 1  # one way to make 0: use no coins

        # 2. fill the table, coin by coin
        for c in coins:              # outer = coin -> fixed order -> combinations
            for a in range(c, amount + 1):   # left to right -> unlimited reuse
                dp[a] += dp[a - c]   # append coin c to every way of making a-c

        return dp[amount]