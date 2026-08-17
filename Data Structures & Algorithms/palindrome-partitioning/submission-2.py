class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(text): 
            i = 0
            j = len(text) - 1 
            while i < j: 
                if text[i] != text[j]: 
                    return False 
                i += 1 
                j -= 1
                
            return True

        def backtrack(start, path): 
            if start >= len(s): 
                res.append(path.copy())
                return
            
            for i in range(start, len(s)): 
                piece = s[start:i+1] 
                if isPalindrome(s[start:i+1]): 
                    path.append(piece)
                    backtrack(i + 1, path) 
                    path.pop()

        backtrack(0, []) 
        return res       
        
            