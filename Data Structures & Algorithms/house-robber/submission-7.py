class Solution:
    def rob(self, nums: List[int]) -> int:
        # don't forget the EDGE CASES that we need base case of 2 elements at least to run algorithm
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
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 
        
        return dp[n-1]
