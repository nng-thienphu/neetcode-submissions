class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Reduction wrapper
        total = sum(nums)
        if total % k != 0:                     
            return False
        target = total // k

        nums.sort(reverse=True)                # PRUNE 1: fail fast — constrained items at shallow depths
        if nums[0] > target:                   
            return False

        buckets = [0] * k                     

        def backtrack(i):                     
            if i == len(nums):                 
                return True
            for pos in range(k):               # decision: WHICH slot, not whether
                if buckets[pos] + nums[i] <= target:  
                    buckets[pos] += nums[i]             # choose
                    if backtrack(i + 1):                # explore
                        return True                     # any one completion suffices (bool/OR)
                    buckets[pos] -= nums[i]             # un-choose
                
                # if the element does not work with an empty slot
                # then no need to test with another empty slot 
                if buckets[pos] == 0:         
                    break                      
            return False                      
        return backtrack(0)