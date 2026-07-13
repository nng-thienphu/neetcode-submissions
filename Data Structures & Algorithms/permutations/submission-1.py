class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        used = [False] * n
        path = []
        result = [] 

        def backtrack(): 
            if len(path) == n: 
                result.append(path.copy()) 
                return 
            
            for j in range(n):  # scan from 0 every time — order matters
                if used[j]: 
                    continue 

                # choose element 
                used[j] = True 
                path.append(nums[j]) 
                # inorder
                backtrack()
                # skip element 
                path.pop()
                used[j] = False
        
        backtrack() 
        return result