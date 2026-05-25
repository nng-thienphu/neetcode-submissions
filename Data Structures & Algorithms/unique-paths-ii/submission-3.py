class Solution:
    # KEY: 
    # My original thought: look at neighbors and decide which direction to "keep moving in."
    # and if meet the node [i][j] == 1, then move to the next one,
    # Nope. this is wrong thought. 

    # LOGIC SOLUTION: 
    # Since if grid[i][j] == 1, then dp[i][j] = 0, return 0 right away, no need to do anything else. 
    # Zero paths can end here, because the cell is unreachable

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # edge case, never start
        if obstacleGrid[0][0] == 1:
            return 0
            
        # set up
        ROWS = len(obstacleGrid) 
        COLS = len(obstacleGrid[0])

        dp = [[0] * COLS for _ in range(ROWS)]

        # What was wrong: 
        # You hardcoded the top row and left column to 1, 
        # assuming there's always exactly one path to those cells. 
        # That's true in the original Unique Paths, but not here — an obstacle upstream in the same row or column cuts off everything after it.
        # Instead, inherit from the one valid neighbor — dp[0][c] = dp[0][c-1] for the top row, dp[r][0] = dp[r-1][0]
        
        dp[0][0] = 1

        for c in range(1, COLS): 
            if obstacleGrid[0][c] == 1:
                dp[0][c] = 0
            else: 
                dp[0][c] = dp[0][c-1] 
        
        for r in range(1, ROWS): 
            if obstacleGrid[r][0] == 1: 
                dp[r][0] = 0
            else: 
                dp[r][0] = dp[r-1][0]

        for r in range(1, ROWS): 
            for c in range(1, COLS): 
                if obstacleGrid[r][c] == 1: 
                    dp[r][c] = 0
                else: 
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[ROWS-1][COLS-1]