class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1":   # this cell is land
                    self.bfs(grid, r, c)
                    result += 1
        
        return result
    
    # KEY INSIGHT: This is a straightforward logic problem.
    # The trick is writing clean code for the 4-directional movement.
    # Instead of four separate if-else blocks, use a directions array:
    #   directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    # and loop over it.
    def bfs(self, grid, row, col): 
        rows = len(grid) 
        cols = len(grid[0])

        queue = deque()
        queue.append([row, col])
        grid[row][col] = "0"

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:    
            r, c = queue.popleft() 

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1": 
                    grid[nr][nc] = "0"
                    queue.append([nr, nc])