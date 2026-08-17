class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0: 
            return max(nums) 
        
        currMax, globMax = 0,0
        currMin, globMin = 0,0

        for i in range(len(nums)): 
            currMax = max(nums[i], nums[i] + currMax) 
            globMax = max(currMax, globMax) 

            currMin = min(nums[i], nums[i] + currMin) 
            globMin = min(currMin, globMin)
        
        return max(globMax, sum(nums) - globMin)
