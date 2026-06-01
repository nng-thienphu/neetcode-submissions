class NumMatrix:

    # KEY 1: 
    # prefix[i][j] = sum of every element inside the rectangle from (0,0) to (i,j)
    # -> create a rectangle of the result as always, not break in the middle
    #
    # KEY 2: 
    #  (0,0) ───────────---──────┐
    #   │      A      │    B     │
    #   │             │          │
    #   ├────────(r1,c1)─────────┤
    #   │      C      │  RED     │
    #   │             │  (r2,c2) │
    #   └─────────────┴──────────┘
    # prefix[r2][c2]   = A + B + C + RED
    # prefix[r1-1][c2] = A + B 
    # prefix[r2][c1-1] = A + C 
    # prefix[r1-1][c1-1] = A
    # RED = total − (A+B) − (A+C) + A

    # KEY 3: 
    # The template code for prefix sum always check < 0
    # since we need to += array[left-1] 
    # We need to the PREFIX MATRIX with a new zero row and column 
    # so the formula never has to handle row 0 or col 0 as special cases 

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix = [[0]*(COLS+1) for _ in range(ROWS + 1)] 
        total = 0 

        for r in range(ROWS): 
            prefix = 0 
            for c in range(COLS): 
                prefix += matrix[r][c]  # CALCULATE THE PREFIX FOR CURRENT DIFFERENT ROW 
                above = self.prefix[r][c+1] # calculate the above row 
                self.prefix[r+1][c+1] = prefix + above # current prefix row + above prefix row
                
        print(f"self.prefix: {self.prefix}")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        all_region = self.prefix[row2][col2] 
        a_c_region = self.prefix[row2][col1-1]
        a_b_region = self.prefix[row1-1][col2]
        a_region = self.prefix[row1-1][col1-1]

        result = all_region - a_c_region - a_b_region + a_region

        return result
            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)