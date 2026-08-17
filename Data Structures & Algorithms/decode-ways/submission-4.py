class Solution:
    def numDecodings(self, s: str) -> int:
        # base case and state
        n = len(s) 
        dp = [0] * (n+1) # include empty string "" + [1...n]
        dp[0] = 1 
        dp[1] = 1 if s[0] != "0" else 0 

        # fill in the table 
        for i in range(2, n+1): 
            oneDigit = int(s[i-1:i])
            twoDigit = int(s[i-2:i])

            if oneDigit >= 1:  
                dp[i] += dp[i-1] 

            if 10 <= twoDigit <= 26: 
                dp[i] += dp[i-2]
            
        return dp[n]
        
