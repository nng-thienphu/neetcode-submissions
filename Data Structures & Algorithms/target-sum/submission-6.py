class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0 

        def backtrack(i, currTotal): 
            nonlocal count 

            if i == len(nums): 
                if currTotal == target: 
                    count += 1
                return 
            
            backtrack(i+1, currTotal + nums[i])
            backtrack(i+1, currTotal - nums[i])

        backtrack(0, 0)
        return count
