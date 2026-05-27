class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = [c for c in s if c.isalnum()]
        # print(text) 

        l = 0 
        r = len(text) - 1 
        while l <= r: 
            # print(f"left: {l, text[l]}, right: {r, text[r]}")
            if text[l].lower() != text[r].lower() : 
                return False
            l += 1
            r -= 1
        
        return True 