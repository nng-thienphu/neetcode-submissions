class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for i in range(n):
            cur_sum = 0
            for j in range(i, i + n):
                cur_sum += nums[j % n]
                res = max(res, cur_sum)

        return res