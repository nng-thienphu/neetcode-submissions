class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums) 
        if total % k != 0: 
            return False
        target = sum(nums) // k

        result = [0] * k 

        def backtrack(i): 
            if i == len(nums): 
                return True

            for pos in range(k): 
                if result[pos] + nums[i] <= target: 
                    result[pos] += nums[i] 
                    if backtrack(i+1): 
                        return True
                    result[pos] -= nums[i] 
                    if result[pos] == 0: 
                        break
        
            return False
        
        return backtrack(0)
                