class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0 
        visit = set()

        for R in range(len(nums)): 
            if R-L > k: 
                visit.remove(nums[L])
                L += 1 
            if nums[R] in visit: 
                return True
            visit.add(nums[R])
        
        return False 

            