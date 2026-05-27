class Solution:
    # WRONG ASSUMPTION: 
    # I read the problem as: "figure out the unique values and return them." That
    #.But the problem is actually asking something different and stricter: mutate the input array in-place so its first k slots hold the unique values, then return k.          
    # 
    # KEY: use two pointer for this problem: 
    # validity: compare the nums[i] and nums[i-1]
    #     Pointer 1: where the next unique value should be written 
    #.    Pointer 2: scan forward through the array looking for new values to write
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        # 1, 1, 1, 2
        
        for r in range(1, len(nums)): 
            if nums[r] != nums[r-1]: 
                nums[l] = nums[r]
                l += 1
        return l 
