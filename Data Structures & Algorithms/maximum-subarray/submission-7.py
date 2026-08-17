class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, glob = nums[0], nums[0] 

        for i in range(1, len(nums)): 
            curr = max(nums[i], nums[i] + curr) 
            glob = max(curr, glob) 
        
 
        return glob
