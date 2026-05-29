class Solution:
    # METHOD 2: use 1 prefix array
    # WRONG ASSUMPTION:
    #   Thought I needed two prefix arrays (left-to-right and right-to-left)
    #   and compare them. Works but O(n) space and off-by-one prone.
    #
    # KEY INSIGHT:
    #   total = left_sum + nums[i] + right_sum
    #   → right_sum = total - left_sum - nums[i]
    #   One total + one running left_sum is enough. No second array.

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) 
        left_sum = 0 

        for i in range(len(nums)): 
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum: 
                return i

            left_sum += nums[i] 
        
        return -1