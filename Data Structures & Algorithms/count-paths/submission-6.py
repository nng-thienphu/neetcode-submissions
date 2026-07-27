class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n 
        memo = {} 
        count = 0 

        def dfs(r, c): 
            if (r,c) in memo: 
                return memo[(r,c)]
            if min(r, c) < 0 or r >= ROWS or c >= COLS: 
                return 0 
            if r == ROWS - 1 and c == COLS -1:
                return 1 
            
            down = dfs(r+1, c) 
            right = dfs(r, c+1)
            memo[(r,c)] = right + down 

            return memo[(r,c)]

        return dfs(0,0)

