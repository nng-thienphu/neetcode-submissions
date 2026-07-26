class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {} 

        def dp(i, remain): 
            if i == n: 
                return 1 if remain == 0 else 0 

            if (i, remain) in memo: 
                return memo[(i, remain)] 
                        
            memo[(i, remain)] = dp(i+1, remain - nums[i]) + dp(i+1, remain + nums[i])
            
            return memo[(i, remain)]
        return dp(0 , target)