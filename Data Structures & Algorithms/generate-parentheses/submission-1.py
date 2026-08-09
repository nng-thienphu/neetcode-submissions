class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, opened, closed):
            if len(path) == 2 * n: 
                res.append(''.join(path)) 
                return

            for char in ['(', ')']: 
                if char == "(": 
                    new_o, new_c = opened + 1, closed
                else: 
                    new_o, new_c = opened, closed + 1
                
                if new_c <= new_o and new_o <= n: 
                    path.append(char)
                    backtrack(path, new_o, new_c) 
                    path.pop()
            
        backtrack([], 0, 0)
        return res 
                

