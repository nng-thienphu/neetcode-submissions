class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 1

        while r <= len(nums)-1: 
            if r < len(nums) - 1 and nums[r] == nums[r+1]:
                count += 1

            else: 
                if count >= 2: 
                    for i in range(2):  
                        nums[l] = nums[r]
                        l += 1 
                else: 
                    nums[l] = nums[r]
                    l+= 1 
                
                count = 1 

            r += 1 
        return l    