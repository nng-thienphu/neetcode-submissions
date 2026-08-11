class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[-1,0], [1,0], [0,1],[0,-1]]
        visited = set()

        def dfs(r,c): 
            if min(r,c)<0 or r >= ROWS or c >= COLS or grid[r][c] == 1: 
                return 0
            if (r,c) in visited: 
                return 0 
            if r == ROWS -1 and c == COLS-1: 
                return 1 

            visited.add((r,c)) 
            path = 0

            for dr, dc in DIRECTIONS: 
                nr, nc = r+dr, c+dc
                path += dfs(nr, nc)  

            visited.remove((r,c)) 
            return path
        
        return dfs(0,0)
        
        