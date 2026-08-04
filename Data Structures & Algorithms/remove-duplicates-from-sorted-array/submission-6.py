class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # COMMON MISTAKES: 
        # you don't handle index 0 in the loop at all. You admit it for free, before the loop starts
        # BECAUSE The first element has nothing earlier, so it cannot be a duplicate  
        left = 1 

        for right in range(1, len(nums)): 
            if nums[right] != nums[left -1]: 
                nums[left] = nums[right] 
                left += 1
        
        return left 