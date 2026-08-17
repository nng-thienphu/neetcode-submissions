class Solution:
    # KEY INSIGHTS : since houses 0 and n−1 can't both be robbed, 
    # at least one of them is skipped in any valid answer. 
    # So split into two scenarios and take the best:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:(n-1)]))
    
    def helper(self, nums): 
        # edge case
        n = len(nums) 
        if n == 0: 
            return 0
        if n == 1: 
            return nums[0] 

        # 1. base case + state 
        dp = [0] * n
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])

        # 2. fill in the table
        for i in range(2, n): 
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]) 
        
        return dp[n-1]
