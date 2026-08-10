class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return
            grid[r][c] = 0
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)

        # Phase 1: sink everything reachable from the border
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1
        return count