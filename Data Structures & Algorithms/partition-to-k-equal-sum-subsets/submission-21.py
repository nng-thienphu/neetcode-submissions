class Solution:
    ''' 
    fits bucket 0        → place there, go deeper
doesn't fit 0, fits 1 → place in 1, go deeper
fits NO bucket        → loop ends → return False  ← the "stuck" signal 
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Reduction wrapper
        total = sum(nums)
        if total % k != 0:                    
            return False
        target = total // k

        nums.sort(reverse=True)                # PRUNE 1: fail fast 
        if nums[0] > target:                  
            return False

        buckets = [0] * k                      # working state: k bucket sums 

        def backtrack(i):                    
            if i == len(nums):                 
                return True
            for pos in range(k):              
                if buckets[pos] + nums[i] <= target:    # bouncer: overflow never happens
                    buckets[pos] += nums[i]             # choose
                    if backtrack(i + 1):                # explore
                        return True              
                    buckets[pos] -= nums[i]             # un-choose
                if buckets[pos] == 0:          
                    break                     
            return False                      
        return backtrack(0)
            