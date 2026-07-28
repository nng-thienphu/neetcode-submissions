class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle) 
        inf = float("inf")
        dp = [[inf] * (row + 1) for r in range(row + 1)] 
        dp[0][1] = 0

        for r in range(1, row + 1): 
            for c in range(0, r+1): 
                up_left =  dp[r-1][c-1]
                up_right = dp[r-1][c] 
                
                dp[r][c] = min(up_left, up_right) + triangle[r-1][c-1]

        return min(dp[row])