class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
            
        memo = {} 

        
        def dp(i, flag, memo): 
            if flag == False: 
                if i == len(nums) - 1: 
                    return 0 

            # check memo
            if (i,flag) in memo:
                return memo[(i,flag)] 

            # edge case
            if i >= len(nums): 
                return 0

            # recursion
            skip = dp(i+1, flag, memo) 
            choose = nums[i] + dp(i+2, flag, memo)
            result = max(skip, choose)
            memo[(i, flag)] = result

            # return
            return memo[(i,flag)]
        
        global_max = max(dp(0, False, memo), dp(1, True, memo))
        return global_max

