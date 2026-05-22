class Solution:
    # KEY 1: We don't need to take a min. 
    #.      BFS gives you the min for free.

    # KEY 2: Don't BFS from the land cells. 
    #      BFS from the treasures, all at the same time

    # KEY 3: Stick with BFS + layer counter techniques 
    #.     there is a lot of BFS code approach
    #.     but stick to the original template please
    # (1) len(queue) as size -> then (2) run for loop around this size

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # set up and set directions
        ROWS = len(grid) 
        COLS = len(grid[0]) 
        directions = [
            (-1,0), (1,0), (0,1), (0,-1)
        ]
        length = 1
        INF = 2147483647

        # init queue and run BFS from treasury cell first
        queue = deque() 
        for r in range(ROWS) : 
            for c in range(COLS): 
                if grid[r][c] == 0: 
                    queue.append((r,c))

        # run while loop for BFS 
        while queue: 
            # 1. run layer by layer -> take length of current queue
            size = len(queue) 

            for _ in range(size): 
                # 2. popleft from queue
                r, c = queue.popleft()

                # 3. logic to move 4 directions 
                for dr, dc in directions: 
                    nr, nc = r+dr, c+dc
                    if (0<=nr<ROWS) and (0<=nc<COLS) and (grid[nr][nc] == INF): 
                        queue.append((nr, nc))
                        grid[nr][nc] = length 
            length +=1 
                
                


