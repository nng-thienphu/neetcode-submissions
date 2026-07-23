class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. dp and base state
        dp = [0] * (amount + 1)
        dp[0] = 1  # one way to make 0: use no coins

        # 2. logic
            # After coin c's pass: dp[a] = number of combinations making a using only the coins processed {1...c} so far.

            # After pass	dp[4]	Meaning
            # c=1	1	ways to make 4 using only {1} — just {1+1+1+1}.  -> dp[4] = 1
            # c=2	3	ways using {1, 2} — adds {1+1+2}, {2+2}.         -> dp[4] = 3 
            # c=3	4	ways using {1, 2, 3} — adds {1+3}                -> dp[4] = 4 
        for c in coins:              # outer = coin -> fixed order -> combinations
            for a in range(c, amount + 1):   # left to right -> unlimited reuse
                dp[a] += dp[a - c]   # append coin c to every way of making a-c

        return dp[amount]