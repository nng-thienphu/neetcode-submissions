class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        for right in range(2, len(nums)): 
            if nums[right] != nums[left-2]: 
                nums[left] = nums[right] 
                left += 1
            
        
        return left