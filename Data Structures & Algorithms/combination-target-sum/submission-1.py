class Solution:
    # KEY: This is final clean code verion
    #     this is normal backtracking problem
    #.    try to understand the template of backtracking
    #.     2 choices, dfs the 1st choice until no more
    #.        then move to the second choice
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output= [] 

        # i: index at nums[i]
        # remaining: how much left to reach 
        # path: list of what we have built so far at the leaf node
        def dfs(i, remaining, path): 
            # successful base case
            if remaining == 0: 
                output.append(path.copy())
                return
            # failed base case 
            if remaining < 0 or i == len(nums): 
                return 

            # choice 1: take one copy of nums[i], stay at i
            path.append(nums[i]) 
            dfs(i, remaining - nums[i], path)

            # choice 2: remove one, and move to the next element
            path.pop()
            dfs(i+1, remaining, path)
                
        dfs(0, target, []) 
        return output
                
            
        

         