class Solution:
    # KEY INSIGHTS: 
    # DFS-APPROACH: Instead of counting number of squares
    # we can just count shared borders seperately and check each neighbor of every land cell during DFS:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # step 1. init row and col
        ROW = len(grid) - 1 
        COL = len(grid[0]) - 1 

        # step 2. run dfs on row and col
        def dfs(row, col, grid): 
            # base case: (1) out of bounds (2) water
            if row > ROW or col > COL or row < 0 or col < 0: 
                return 1 

            if grid[row][col] == -1: 
                return 0 
            
            if grid[row][col] == 0: 
                return 1 

            # mark visit: 
            grid[row][col] = -1

            # moving 4 directions 
            total = 0
            directions = [(-1,0), (1, 0), (0,1), (0,-1)]
            for dr, dc in directions: 
                total += dfs(row + dr, col + dc, grid) 
            
            return total 
        
        # KEY CODE TECHNIQUE: 
        # the total should be return inside this for loop 
        # since once you find the first land cell and run DFS on it, 
        # DFS visits the entire island and accumulates the full perimeter into total
        for r in range(ROW+1): 
            for c in range(COL+1): 
                if grid[r][c] == 1:
                    return dfs(r,c,grid)

        return 0

