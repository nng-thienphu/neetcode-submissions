class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = globMax = nums[0] 
        currMin = globMin = nums[0] 

        for i in range(1, len(nums)): 
            currMax = max(nums[i], nums[i] + currMax) 
            globMax = max(globMax, currMax) 

            currMin = min(nums[i], nums[i] + currMin) 
            globMin = min(globMin, currMin) 

        if globMax < 0: 
            return globMax

        return max(globMax, sum(nums) - globMin)