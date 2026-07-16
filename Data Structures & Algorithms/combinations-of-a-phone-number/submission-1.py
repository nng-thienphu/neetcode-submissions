class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Type: this problem is combinations backtracking since (1) "Find all" (2) "dg" = "gd" -> eliminate
        #.  the trick of combination is starting index and never look back
        
        if len(digits) == 0: 
            return [] 

        res = [] 
        path = [] 

        phone = {
            "1": [], 
            "2": ["a", "b", "c"], 
            "3": ["d", "e", "f"], 
            "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"], 
            "7": ["p", "q", "r", "s"], 
            "8": ["t", "u", "v"], 
            "9": ["w", "x", "y", "z"] 
        }

        def backtrack(i): 
            if len(path) == len(digits): 
                # print(path)
                res.append("".join(path)) 
                return

            charList = phone[digits[i]] 
            
            for c in charList: 
                path.append(c) 
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return res

