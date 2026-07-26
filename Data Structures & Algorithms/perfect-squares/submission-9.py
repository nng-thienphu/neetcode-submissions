class Solution:
    def numSquares(self, n: int) -> int:
        number = int(math.sqrt(n))
        dp = [[(n+1)] * (n+1) for _ in range(number + 1)] 
            # dp[i][j] = "using only the squares 1² .. i²,
            # what's the minimum count of them that sum to exactly j?""

        for i in range(number+1): 
            dp[i][0] = 0

        for i in range(1, number + 1): 
            square = i ** 2

            for j in range(1, n+1): 
                dp[i][j] = dp[i-1][j]  # don't use any new number, skip

                if j >= square: 
                    dp[i][j] = min(dp[i-1][j], dp[i][j-square] + 1) # use one new number
        
        return dp[number][n]
        