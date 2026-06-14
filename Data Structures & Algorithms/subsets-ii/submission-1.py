class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # KEY: Since the nums contains duplicat
        # so we need to sort it first so we can compare i and i+1 indexed number
        nums.sort()
        resultSubset, currSet = [], [] 

        self.helper2(0, nums, currSet, resultSubset)

        return resultSubset
    
    def helper2(self, i, nums, currSet, resultSubset): 
        if i >= len(nums): 
            resultSubset.append(currSet.copy()) 
            return
        
        # left 
        currSet.append(nums[i]) 
        self.helper2(i+1, nums, currSet, resultSubset) 

        # node
        currSet.pop()

        # right
        # KEY: duplicate check here, only need to compare i and i+1
        while i+1 < len(nums) and nums[i] == nums[i+1]: 
            i+=1 
        self.helper2(i+1, nums, currSet, resultSubset)