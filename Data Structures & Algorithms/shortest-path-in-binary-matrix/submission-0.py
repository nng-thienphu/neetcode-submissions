class Solution:
    # KEY 1: BFS guarantee the first time you reach (n-1, n-1) 
    #.        this is the shortest path

    # KEY 2: The length of the path is not calculated my queue but by layer
    #        template for everything. Template for all BFS algorithm
        # length = 1  # starting cell counts as 1
        # while queue:
        #     size = len(queue)        # how many cells are in this layer
        #     for _ in range(size):    # process exactly this layer
        #         r, c = queue.popleft()
        #         # check if (r,c) is the target
        #         # enqueue valid neighbors
        #     length += 1              # done with this layer, move to next

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # setup: (1) length limitation (2) 8-direction 
        n = len(grid) 
        directions = [
            (-1, -1), (-1, 0), (-1, 1), 
            (0, -1),          (0, 1), 
            (1, -1), (1,0), (1,1)
        ]

        # edge case: start or end is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: 
            return -1

        visited = [[False] * n for _ in range(n)] 
        
        #------- BFS ----- 
        # step 1. bfs, intialize with (1) queue (2) visited array
        queue =    queue = deque([
            (0,0,1) # row, col, distance
        ]) 
        visited = [[False] * n for _ in range(n)] # represent all the pixel in matrix
        visited[0][0] = True     # we are at the beginning of the matrix 

        # step 2. run while loop,
        # -> set (1) pop queue to get element (2) check base case (3) move
        while queue: 
            r, c, dist = queue.popleft()

            # base case: if we reach the end of matrix 
            if r == n -1 and c == n - 1 : 
                return dist

            # step 3. move each layer to each layer, 
            # with (1) edge case checking 
            # with (2) add to queue
            # with (3) add to visited array
    
            for dr, dc in directions: 
                nr, nc = r+dr, c+dc

                # edge case
                # can move if inbound, not visited, and equal 0 
                if(
                    0 <= nr < n and 0 <= nc < n
                    and not visited[nr][nc] 
                    and grid[nr][nc] == 0 
                ): 
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist+1))

        return -1 



