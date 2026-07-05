class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_visited = set() 
        atlantic_visited = set() 
        ROWS, COLS = len(heights), len(heights[0]) 
        DIRECTIONS = [[0,1], [0,-1], [-1,0], [1,0]]
        
        def bfs(r, c, pacific_visit = False): 
            if pacific_visit: 
                visited_set = pacific_visited 
            else: 
                visited_set = atlantic_visited 

            q = deque()
            q.append((r, c))

            while q: 
                row, col = q.popleft()
                visited_set.add((r,c))
                
                for dr, dc in DIRECTIONS: 
                    nr, nc = row + dr, col + dc 

                    # validity check
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited_set or heights[nr][nc] < heights[row][col]:
                        continue 
                    visited_set.add((nr, nc))
                    q.append((nr, nc))

        # run bfs from pacific 
        for c in range(COLS): 
            bfs(0, c, True)
            bfs(ROWS-1, c, False)
        
        for r in range(ROWS): 
            bfs(r, 0, True) 
            bfs(r, COLS-1, False)

        result = [] 
        for r,c in pacific_visited: 
            if (r,c) in atlantic_visited: 
                result.append([r,c])

        # compare the visit of two then return 
        return result
            

    

        

        
    