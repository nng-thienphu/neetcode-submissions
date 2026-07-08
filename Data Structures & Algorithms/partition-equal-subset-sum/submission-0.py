class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0: 
            return False
        target = total / 2
        
        memo = {} 
        def dfs(i, cap): 
            if cap == 0: 
                return True
            if i >= len(nums) or cap < 0:  #  ran out of items, or overshot
                return False 
            if (i, cap) in memo: 
                return memo[(i, cap)]

            # skips item nums[i]
            take = dfs(i+1, cap - nums[i])
            skip = dfs(i+1, cap)
            memo[(i,cap)] = take or skip

            return memo[(i,cap)]
        
        return dfs(0, target)


