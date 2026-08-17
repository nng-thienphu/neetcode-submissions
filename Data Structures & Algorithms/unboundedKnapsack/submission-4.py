class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[-1] * (capacity+1) for _ in range(len(weight)+1)] 
        
        def dp(i, rc): 
            if i == 0: 
                return 0 

            if memo[i][rc] != -1: 
                return memo[i][rc] 

            skip = dp(i-1, rc) 
            take = float("-inf") 
            if weight[i-1] <= rc: 
                take = dp(i, rc-weight[i-1]) + profit[i-1]

            memo[i][rc] = max(skip, take) 

            return memo[i][rc] 

        return dp(len(weight), capacity)