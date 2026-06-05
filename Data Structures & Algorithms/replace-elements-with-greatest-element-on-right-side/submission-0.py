class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = -1
        new_arr = [-1] * len(arr) # [-1, -1, -1, -1...]

        # run from right to left
        for i in range(len(arr)-1, -1, -1): 
            if i!=len(arr)-1 and arr[i+1] > best: 
                best = arr[i+1] 
            new_arr[i] = best
        
        return new_arr


        

            
