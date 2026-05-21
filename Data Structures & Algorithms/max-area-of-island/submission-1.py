class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # setup 
        ROWS = len(grid) 
        COLS = len(grid[0]) 
        max_islands = 0 

        def dfs(r,c): 
            # Base case: 
            # 1. out of matrix
            # 2. pixel is water 
            if (
                min(r,c) < 0 or
                r >= ROWS or  
                c >= COLS or 
                grid[r][c] == 0
            ): 
                return 0 
            
            # Mark visited: change from 1 to 0  
            grid[r][c] = 0 

            # Dfs logic: move in 4 direction
            up = dfs(r+1, c)
            down = dfs(r-1, c) 
            right = dfs(r, c+1)
            left = dfs(r, c-1)

            return 1 + up + down + right + left 
            

        # find the first 1: 
        for r in range(ROWS): 
            for c in range(COLS): 
                # first 1 found, run dfs and take max 
                if grid[r][c] == 1: 
                    max_islands = max(max_islands, dfs(r,c))

        return max_islands 
        
            

