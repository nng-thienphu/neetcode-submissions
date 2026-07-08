class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}   # (i, cap) -> best profit using items i.. with cap room left

        def dfs(i, cap):
            if i >= len(profit):            # no items left
                return 0
            if (i, cap) in memo:
                return memo[(i, cap)]

            # skip item i
            best = dfs(i + 1, cap)

            # take item i — only if it fits
            if weight[i] <= cap:
                best = max(best, profit[i] + dfs(i + 1, cap - weight[i]))

            memo[(i, cap)] = best
            return best

        return dfs(0, capacity)