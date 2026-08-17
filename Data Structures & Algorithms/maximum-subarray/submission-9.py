class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for r in range(1, len(nums)): 
            curr = max(nums[r], curr + nums[r])
            best = max(best, curr)
        
        return best
