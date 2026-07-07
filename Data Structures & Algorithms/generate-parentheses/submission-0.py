class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, part = [], []
        
        def dfs(open_count, close_count): 
            # base case: all 2n characters places 
            if open_count == close_count == n: 
                res.append("".join(part)) 
                return
            
            # add '(' — only if budget of n opens remains
            if open_count < n: 
                part.append("(") 
                dfs(open_count + 1, close_count) 
                part.pop()

            # add ')' — only if there's an unmatched '(' to close
            if close_count < open_count:
                part.append(")")
                dfs(open_count, close_count + 1)
                part.pop()

        dfs(0, 0)
        return res 