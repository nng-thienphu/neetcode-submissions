
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2  # first two elements admitted free: can't be a 3rd copy of anything

        for right in range(2, len(nums)):
            if nums[right] != nums[left - 2]:  # answer region, not raw array
                nums[left] = nums[right]
                left += 1

        return left