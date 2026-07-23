class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for s in range(1, i + 1):        # i + 1 → includes s = i, so i = 1 tries s = 1
                remain = i - s * s
                if remain < 0:               # s² overshot i → all bigger s overshoot too
                    break
                dp[i] = min(dp[i], 1 + dp[remain])

        return dp[n]