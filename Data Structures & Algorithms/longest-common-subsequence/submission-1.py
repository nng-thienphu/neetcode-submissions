class Solution:
    # KEY 1 LOGIC: 
    # tabulation approach the whole 2 string  
    # at every step, you're looking at one pair of characters text1[i] and text2[j]:
    # They match: move diagonally 
    # The dont match: move one side only 

    # KEY 2 BASE CASE: 
    # when one of the strings is fully consumed 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2) 

        # text 1 is the row
        # text 2 is the column
        dp = [[0] * (n+1) for _ in range(m+1)] 

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]


            
        
