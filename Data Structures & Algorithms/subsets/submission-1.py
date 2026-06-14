class Solution:
    # KEY: The key to solve this problem is that
    # Use one shared CURRENT [] list across all recursive calls, 
    # mutating it with append then undoing with pop after each "include" branch 
    # this is the backtracking st…Use one shared current list across all recursive calls
    # mutating it with append then undoing with pop after each "include" branch 
    # this is the backtracking step that keeps current in sync with the path you're walking in the tree
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetResult, currSet = [], []
        self.helper(0, nums, currSet, subsetResult)

        return subsetResult
    
    def helper(self, i, nums, currSet, subsetResult):
        if i >= len(nums): 
            subsetResult.append(currSet.copy())
            # copy() because curSet is mutated later 
            
            return
        
        # left 
        currSet.append(nums[i]) 
        self.helper(i+1, nums, currSet, subsetResult)

        # node - backtrack
        currSet.pop()

        # right
        self.helper(i+1, nums,currSet, subsetResult)



