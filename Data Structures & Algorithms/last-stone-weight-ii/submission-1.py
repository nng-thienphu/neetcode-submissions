class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones) 
        target = total // 2 

        # dp[i][j]
        #.  = "using only the first i stones, what's the largest subset sum achievable without exceeding j?"
        n = len(stones)
        dp = [[0] * (target+1) for _ in range(n+1)]

        for i in range(1, n+1): 
            w = stones[i-1] 
            for j in range(1, target + 1): 
                dp[i][j] = dp[i-1][j]

                if j >= w: 
                    dp[i][j] = max(dp[i-1][j-w] + w, dp[i-1][j]) 
                
        return total - 2 * dp[n][target]