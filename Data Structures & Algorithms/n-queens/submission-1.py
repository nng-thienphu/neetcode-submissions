class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] 
        path = []
        cols, diag1, diag2 = set(), set(), set()

        def is_valid(row, col):
            return (col not in cols
                    and (row - col) not in diag1
                    and (row + col) not in diag2)


        def remove(row, col): 
            path.pop()
            cols.remove(col) 
            diag1.remove(row-col) 
            diag2.remove(row+col)            
        
        def add(row, col): 
            path.append(col)
            cols.add(col) 
            diag1.add(row-col) 
            diag2.add(row+col)

        def backtrack(row): 
            if row == n : 
                board = [] 
                for c in path :
                    left = '.' * c 
                    right = '.' * (n-c-1) 
                    board.append(left+'Q'+right)
                res.append(board) 
                return 

            for col in range(n): 
                if is_valid(row, col) : 
                    add(row, col) 
                    backtrack(row+1) 
                    remove(row, col) 
            
        backtrack(0) 
        return res 

