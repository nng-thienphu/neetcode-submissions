class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0 
        best = float("-inf")

        for r in range(len(nums)): 
            curr = max(nums[r], curr + nums[r])
            best = max(best, curr)
        
        return best

            

