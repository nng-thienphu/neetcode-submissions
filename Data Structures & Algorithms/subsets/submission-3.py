class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, part = [], [] 

        def dfs(i):
            if i == len(nums): 
                result.append(part.copy())
                return result
            
            part.append(nums[i])
            dfs(i+1) 

            part.pop()
            dfs(i+1)
        
        dfs(0)
        return result