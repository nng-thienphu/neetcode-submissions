class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # setup
        # 1. lens -> limitation for position
        ROWS, COLS = len(image), len(image[0])
        starting_color = image[sr][sc]
        # 2. guard 
        # if the starting color = color -> no need to change as everything is the same 
        if starting_color == color:
            return image

        def dfs(r, c): 
            # Base case
            # 1. Out of matrix: <0 or >LENS
            # 2. Already visit pixel: (r,c) has already visited
            # 3. Pixel blocked : image[r][c] != image[start_row][start_col] 
            if(
                min(r,c) < 0 or
                r >= ROWS or
                c >= COLS or
                image[r][c] != starting_color
           ): 
                return 
            
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image

        



