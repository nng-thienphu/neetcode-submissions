class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check the row 
        # the trick of this problem is to consider the end element of the row
        #     and also consider the first element of the row

        # the trick of binary search is that 
           # the left side = mid + 1 
           # and the right side = mid - 1
        top = 0
        bot = len(matrix) - 1 
        row = 0 
        while top <= bot: 
            row = (top + bot) // 2
            if target > matrix[row][-1]: 
                top = row + 1
            elif target < matrix[row][0]: 
                bot = row - 1 
            else: 
                break 
        
        # Need to check after row binary search
        if top > bot: 
            return False 
        
        lo = 0
        hi = len(matrix[row]) - 1 
        while lo <= hi:
            col =  (lo + hi) // 2

            if target > matrix[row][col]: 
                lo = col + 1
            elif target < matrix[row][col]: 
                hi = col - 1
            else: 
                return True
        
        return False
        
