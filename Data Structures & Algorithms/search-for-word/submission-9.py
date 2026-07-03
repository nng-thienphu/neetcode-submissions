class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # init rows and col 
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        # write dfs function
        def dfs(row, col, i): 
            # base case: 
            if min(row, col) < 0 or row >= ROWS or col >= COLS or board[row][col] != word[i]:
                return False
            
            if (row, col) in visited:
                return False

            if i == len(word) - 1 and board[row][col] == word[len(word) - 1]:
                # # print(i)
                # print(board[row][col])
                return True

            # recursion
            visited.add((row, col))
            i += 1
            a = dfs(row+1, col, i)
            b = dfs(row-1, col, i)
            c = dfs(row, col+1, i)
            d = dfs(row, col-1, i)
            visited.remove((row, col)) 

            if a or b or c or d: 
                return True
            else: 
                return False 
            

        # loop to find the first chracter in word, then run dfs
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == word[0]: 
                    if dfs(r, c, 0):     # only bail out on success
                        return True

        return False
