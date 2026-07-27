class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0]) 
        dp = [[0]* (COLS) for _ in range(ROWS)] 

        for i in range(ROWS): 
            if obstacleGrid[i][0] == 1: 
                break
            else: 
                dp[i][0] = 1 
        
        for i in range(COLS): 
            if obstacleGrid[0][i] == 1: 
                break
            else: 
                dp[0][i] = 1 

        for r in range(1, ROWS): 
            for c in range(1, COLS): 
                if obstacleGrid[r][c] == 1: 
                    dp[r][c] = 0
                else:
                    down = dp[r-1][c]  
                    right = dp[r][c-1] 

                    dp[r][c] = down + right

        return dp[ROWS-1][COLS-1]