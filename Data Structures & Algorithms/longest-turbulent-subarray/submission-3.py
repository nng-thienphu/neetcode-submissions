class Solution:
    # KEY: 
    # Instead of thinking "do the element zigzag up and down"
    # think, "do the comparision sign (< and >) alternate with each other" 
    # For each adjacent pair in the subarray: 
    # - arr[i] > arr[i+1] -> sign is "+" (up) 
    # - arr[i] < arr[i+1] -> sign is "-" (down) 
    # - arr[i] == arr[i+1] -> sign is "0" (flat)

    # A subarray is turbulent if the signs go: + - + - ... or - + - + ... with no two signs the same and no zeros.
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        best = 1

        for r in range(1, len(arr)): 
            # all reset case
            # reset 1: two element is equal to each other
            if arr[r] == arr[r-1]: 
                print("equal check")
                l = r
                print(f"left:{l}, right:{r}") 
                print("------------------")
            # reset 2: 
            elif (r >= 2) and (arr[r-1]-arr[r-2])*(arr[r]-arr[r-1]) >= 0 : 
                print(f"left:{l}, right:{r}") 
                l = r - 1
            
            best = max(best, r-l +1)
            
        return best             