class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        best = 0

        if max(nums) < 0:
            return max(nums)

        for i in range(0, len(nums)) : 
            curr = max(nums[i], curr + nums[i]) 
            best = max(best, curr) 

        return best  