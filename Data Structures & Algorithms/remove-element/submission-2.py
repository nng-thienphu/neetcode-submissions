class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = right = 0

        for right in range(len(nums)): 
            if nums[right] != val: 
                nums[left] = nums[right] 
                left += 1
            right += 1
        
        return left