class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        used = [False] * n
        path = []
        result = [] 

        def backtrack(): 
            if len(path) == n: 
                result.append(path.copy()) 
            
            for j in range(n): 
                if used[j]: 
                    continue 

                used[j] = True 
                path.append(nums[j]) 
                backtrack()

                path.pop()
                used[j] = False
        
        backtrack() 
        return result