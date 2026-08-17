class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:                 # all negative: wrap illegal, complement would be empty
            return max(nums)              # best = least-bad single element

        total = 0
        currMax, maxSum = 0, nums[0]
        currMin, minSum = 0, nums[0]
        for num in nums:
            currMax = max(num, currMax + num);  maxSum = max(maxSum, currMax)
            currMin = min(num, currMin + num);  minSum = min(minSum, currMin)
            total += num

        return max(maxSum, total - minSum)