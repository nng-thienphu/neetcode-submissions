class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r,c): 
            if min(r,c) < 0 or r>= ROWS or c>= COLS or grid[r][c] == 0: 
                return
            
            grid[r][c] = 0 

            for dr, dc in DIRECTIONS: 
                dfs(r+dr, c+dc) 
        

        for r in range(ROWS): 
            if grid[r][0] == 1: 
                dfs(r,0) 
            if grid[r][COLS-1] == 1: 
                dfs(r,COLS-1) 
        
        for c in range(COLS): 
            if grid[0][c] == 1: 
                dfs(0,c) 
            if grid[ROWS-1][c] == 1: 
                dfs(ROWS-1,c) 
            
        count = 0
        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 1: 
                    count += 1 
        
        return count
        
