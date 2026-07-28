class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2) 
        dp = [[0] * (l1+1) for _ in range(l2+1)] 

        for r in range(1, l2+1): 
            for c in range(1, l1+1): 
                if text2[r-1] == text1[c-1]: 
                    dp[r][c] = dp[r-1][c-1] + 1
                else: 
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1]) 
        
        return dp[l2][l1] 