class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {} 

        def dp(i): 
            if i == len(s): 
                return 1
            if s[i] == "0": 
                return 0
            
            if i in memo: 
                return memo[i] 
            
            single_digit = dp(i+1)

            two_digit = 0 
            if i+1 < len(s) and int(s[i:i+2]) <= 26: 
                two_digit = dp(i+2)

            res = single_digit + two_digit
            memo[i] = res 

            return memo[i]
        return dp(0)