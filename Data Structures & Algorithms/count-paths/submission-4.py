class Solution:
    # METHOD: DEPTH FIRST SEARCH

    # KEY: Using this will cause O(2^(m+n)) time
    # to optimize for time with DFS, should use memoization 

    def uniquePaths(self, m: int, n: int) -> int:

        memo = {} 

        def dfs(row, col): 
            # check memo first
            if(row, col) in memo: 
                return memo[(row, col)]
            # base case
            if row == m-1 and col == n-1: 
                return 1

            # out of bound
            if row >= m or col >= n: 
                return 0

            # recuse on neighbors 
            down = dfs(row+1, col)
            right = dfs(row, col +1)

            result = down + right 

            memo[(row, col)] = result

            return result  

        return dfs(0,0)
