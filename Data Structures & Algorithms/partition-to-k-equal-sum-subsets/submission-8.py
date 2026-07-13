class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums) 
        if total % k != 0: 
            return False
        target = total / k

        nums.sort(reverse = True)
        used = [False] *  n

        def backtrack(i, k, sumSubset): 
            # base case 1: 1 bucket is done, start another new bucket 
            if sumSubset == target: 
                return backtrack(0, k-1, 0)

            # base case 2: all buckets are done 
            if k == 0: 
                return True

            # # base case 1: 1 bucket is done, start another new bucket 
            # if sumSubset == target: 
            #     return backtrack(0, k-1, 0)

            # recursion with used node tracking 
            for j in range(i, len(nums)): 
                if used[j] or sumSubset + nums[j] > target: 
                    continue
                
                # Optimization: skip duplicates
                if j > 0 and not used[j-1] and nums[j] == nums[j-1]:
                    continue

                used[j] = True
                if backtrack(j+1, k, sumSubset + nums[j]):
                    return True
                used[j] = False
            
            return False
        return backtrack(0,k,0)



