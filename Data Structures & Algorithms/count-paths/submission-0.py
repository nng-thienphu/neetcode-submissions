class Solution:
    # METHOD: TABULATION DYNAMIC PROGRAMMING APPROACH
    # KEY 1: The number of ways to reach (i, j) 
    # is the sum of the number of ways to reach each of its two predecessors.
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # KEY 2: Base case:  
    # Base cases: top row and leftmost column all 1s.
    # (think)  reach (0, j), you just walk right j times. There's no other way
    
    def uniquePaths(self, m: int, n: int) -> int:
        # set up: create a matrix of m x n
        dp = [[0]*n] * m

        # base case 
        for c in range(n): 
            dp[0][c] = 1

        for r in range(m): 
            dp[r][0] = 1 
        
        
        for i in range(1, m): 
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        
        return dp[m-1][n-1]

