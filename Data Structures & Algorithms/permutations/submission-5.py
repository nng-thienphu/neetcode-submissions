class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set() 

        def backtrack(path): 
            if len(path) == len(nums):
                res.append(path.copy()) 
                return
            
            for i in range(len(nums)): 
                if i in visited: 
                    continue
                visited.add(i)
                path.append(nums[i])
                backtrack(path) 
                path.pop()
                visited.remove(i)
            
        backtrack([]) 
        return res
            