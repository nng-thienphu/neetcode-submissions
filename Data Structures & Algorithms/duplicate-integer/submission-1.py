class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for e in nums: 
            if e in seen: 
                return True
            else: 
                seen.add(e)
        
        return False 