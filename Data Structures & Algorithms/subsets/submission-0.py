class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        current = [] 
    
        def backtrack(i): 
            # base case
            if i == len(nums): 
                result.append(current.copy())
                return
            
            # choice 1: add the number 
            current.append(nums[i])
            backtrack(i+1) 

            # choice 2: don't include the number
            current.pop() 
            backtrack(i+1) 
    
        backtrack(0)

        return result
