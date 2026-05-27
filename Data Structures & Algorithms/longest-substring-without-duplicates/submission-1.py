class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        text = set()
        best = 0

        for r in range(len(s)):            
            # shrink until duplicate is gone     
            while s[r] in text:  
                text.remove(s[l])
                l += 1 
            
            # if not in set, just keep adding text 
            text.add(s[r])
            best = max(best, r - l +1)
            print(f'text: {text}, best: {best}, left: {l}, right {r}, array: {s[l:r+1]}')
        return best