class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        dp = [[-1] * (capacity +1) for _ in range(n+1)] 

        def f(i, rc): 
            if i == 0: 
                return 0
            if dp[i][rc] != -1: 
                return dp[i][rc]
            
            notTake = f(i-1, rc)
            take = float('-inf') 

            if weight[i-1] <= rc: 
                take = profit[i-1] + f(i, rc - weight[i-1])
            
            dp[i][rc] = max(take, notTake)

            return dp[i][rc] 
        
        return f(n, capacity)

            