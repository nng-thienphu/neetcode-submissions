class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)] 
        col_set = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 

        for r in range(9):
            for c in range(9): 
                val = board[r][c] 

                if val == "." :
                    continue
                
                # // -> always round down
                # 0 // 3  # 0
                # 1 // 3  # 0
                # 2 // 3  # 0
                # 3 // 3  # 1
                # 4 // 3  # 1
                # 5 // 3  # 1
                # 6 // 3  # 2
                # 7 // 3  # 2
                # 8 // 3  # 2
                box_idx = (r//3) * 3 + (c//3) 

                if val in row_set[r] or val in col_set[c] or val in boxes[box_idx]: 
                    return False

                row_set[r].add(val)
                col_set[c].add(val) 
                boxes[box_idx].add(val) 


        return True