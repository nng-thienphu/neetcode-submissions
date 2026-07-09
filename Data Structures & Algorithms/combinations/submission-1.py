class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracking(i, path): 
            # KEY: 
            # i = first number we are ALLOWED to pick (forward only)
            # path  = numbers chosen so far on this branch

            if len(path) == k: 
                result.append(path.copy()) 
                return
            if i > n: 
                return 
            path.append(i) 
            backtracking(i+1, path) 
            path.pop() 
            backtracking(i+1, path) 
        
        backtracking(1, []) 
        return result