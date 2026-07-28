class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1] * (r+1) for r in range(numRows)] 
                
        for r in range(2, numRows): 
            for c in range(1, r): 
                up_left = tri[r-1][c-1]
                up_right = tri[r-1][c]
                tri[r][c] = up_left + up_right 
            
        
        return tri