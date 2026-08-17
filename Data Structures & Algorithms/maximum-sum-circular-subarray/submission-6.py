class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, globMax = nums[0], nums[0] 
        currMin, globMin = nums[0], nums[0] 
        total = sum(nums)

        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax + nums[i]) 
            globMax = max(currMax, globMax) 

            currMin = min(nums[i], currMin + nums[i]) 
            globMin = min(currMin, globMin) 
        
        if globMax < 0: 
            return globMax
        
        return max(globMax, total - globMin)