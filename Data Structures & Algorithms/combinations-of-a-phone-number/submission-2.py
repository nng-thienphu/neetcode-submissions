class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Type: this problem is combinations backtracking since (1) "Find all" (2) "dg" = "gd" -> eliminate
        #.  the trick of combination is starting index and never look back
        
        if len(digits) == 0: 
            return [] 

        res = [] 
        path = [] 

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
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

