class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]] 
        for i in range(1, numRows): # pass the first row so we can i-1 vaid
            curr_row = [1] # the first element always be there
            prev = result[i - 1]
            for j in range(1, len(prev)): 
                curr_row.append(prev[j-1] + prev[j]) 
            curr_row.append(1) # add the last element since it is always 1 + 0 
            result.append(curr_row) 
        
        return result


# dp[i] = answer for prefix ending at index i
# dp = [0] * (n + 1)  # or same len as input
# dp[0] = base_case

# for i in range(1, n + 1):
#     # transition looks back a constant number of steps
#     dp[i] = min/max/sum(dp[i-1], dp[i-2], ...)  # + cost[i]

# return dp[n]
