class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = -1
        new_arr = [0] * len(arr) # [-1, -1, -1, -1...]

        # run from right to left
        for i in range(len(arr)-1, -1, -1): 
            new_arr[i] = best
            best = max(arr[i], best)
        
        return new_arr


        

            
