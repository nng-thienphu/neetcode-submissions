class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        return self.dfs(0, profit, weight, capacity, memo)

    def dfs(self, idx, profit, weight, capacity, memo): 
        if idx >= len(profit): 
            return 0
        
        if (idx, capacity) in memo:  
            return memo[(idx, capacity)]
        
        # Option 1: Include item (if it fits)
        take = 0
        if capacity - weight[idx] >= 0: 
            take = profit[idx] + self.dfs(idx+1, profit, weight, capacity - weight[idx], memo)
        
        # Option 2: Skip item
        skip = self.dfs(idx+1, profit, weight, capacity, memo)

        memo[(idx, capacity)] = max(take, skip) 
        return memo[(idx,capacity)]
