class Solution:
    # KEY INSIGHTS: the case for mismatch, run the min between these: 
    #     replace a[i-1] with b[j-1]: both consumed 
    #     delete a[i-1]: only a gave up a character -> look up 
    #     insert b[j-1]: only b gave up a character -> look left 
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2) 
        dp = [[0] * (n+1) for _ in range(m+1)] 
        
        # ---- base column: b[:0] is empty, so delete everything in a[:i] ----
        #   because dp[i][j] mean min operations to turn a[:i] into b[:j] 
        for i in range(m+1): 
            dp[i][0] = i 
        for j in range(n+1): 
            dp[0][j] = j 

        # ---- fill in the interios, top-left to bottom-right ---- 
        for i in range(1, m+1): 
            for j in range(1, n+1): 
                # case 1 - match: no operation need
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1]
                # case 2 - mis-match: so ONE operation is unavoidable, try 3 operation at the same time
                else: 
                    up = dp[i-1][j]
                    diag = dp[i-1][j-1]
                    left = dp[i][j-1] 
                    
                    dp[i][j] = 1 + min(up, diag, left) 
        
        return dp[m][n]