from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo = {}

        def dp(i, flag):
            # flag=False → last house is off-limits (Case A)
            if flag == False and i == n - 1:
                return 0
            if i >= n:
                return 0
            if (i, flag) in memo:
                return memo[(i, flag)]

            skip = dp(i + 1, flag)
            choose = nums[i] + dp(i + 2, flag)
            memo[(i, flag)] = max(skip, choose)
            return memo[(i, flag)]

        return max(dp(0, False), dp(1, True))