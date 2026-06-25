class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        global_max = 0

        left = 0 
        right = len(nums) - 1 

        nums.sort()

        while left < right: 
            if nums[left] + nums[right] >= k: 
                right -= 1
            else: 
                global_max = max(nums[left] + nums[right], global_max)
                left += 1

        return global_max if global_max > 0 else -1 