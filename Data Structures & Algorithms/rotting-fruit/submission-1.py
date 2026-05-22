class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid) 
        COLS = len(grid[0]) 
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        queue = deque()
        
        for r in range(ROWS) :
            for c in range(COLS): 
                if grid[r][c] == 2: 
                    queue.append((r,c)) 
        
        length = 0
        while queue: 
            size = len(queue) 
            did_rot = False

            for _ in range(size): 
                r,c = queue.popleft()
                for dr, dc in directions: 
                    nr, nc = r+dr, c+dc
                    if((0<=nr<ROWS) and (0<=nc<COLS) and (grid[nr][nc]==1)): 
                        grid[nr][nc] = 2 
                        queue.append((nr, nc))
                        did_rot = True
            # need to guard if we really change, otherwise 1 redudant case at the end
            if did_rot: 
                length += 1
        
        # check if there still unreachable fruit
        for row in grid : 
            if 1 in row: 
                return -1

        return length