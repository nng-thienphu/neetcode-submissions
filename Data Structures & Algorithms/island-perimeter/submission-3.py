from typing import List

class Solution:
    # KEY INSIGHTS: 
    # DFS-APPROACH: Instead of counting number of squares,
    # we can just count shared borders separately and check each neighbor of every land cell during DFS:
    # - neighbor is water or out of bounds -> +1 to perimeter
    # - neighbor is land -> +0 (shared border, doesn't count)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW = len(grid) - 1 
        COL = len(grid[0]) - 1 
        DIRECTIONS = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(row, col): 
            # base case: (1) out of bounds (2) water -> contributes 1 edge
            if row > ROW or col > COL or row < 0 or col < 0: 
                return 1 
            if grid[row][col] == -1: 
                return 0 
            if grid[row][col] == 0: 
                return 1 

            # mark visited
            grid[row][col] = -1

            # moving 4 directions, accumulate perimeter
            total = 0
            for dr, dc in DIRECTIONS: 
                total += dfs(row + dr, col + dc) 
            return total 
        
        # KEY CODE TECHNIQUE: 
        # return total inside the loop since there is exactly one island —
        # once you find the first land cell and run DFS on it,
        # DFS visits the entire island and accumulates the full perimeter
        for r in range(ROW+1): 
            for c in range(COL+1): 
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0