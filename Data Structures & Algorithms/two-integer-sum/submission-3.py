class Solution:
    # KEY 1: enumerate(nums) pairs each element with its index
    #.        for i, n in enumerate(nums) = (index, nums[index]) 

    # KEY 2: Duplicate problem. Hashmaps can't hold two entries for the same key — assigning to an existing key overwrites it. So pre-loading the whole array first ([5, 5]) loses index 0 and you return [1, 1], violating i != j.
    #.        solution: insert after works. The invariant: at iteration i, seen contains only elements strictly before i. So a hit on y in seen is guaranteed to be a different, earlier index. You don't miss any pair (i, j) with i < j 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        # key 1: use enumerate
        for i, x in enumerate(nums): 
            y = target - x

            if y in hashmap: 
                return [hashmap[y], i]
            
            # key 2: insert after 
            hashmap[x] = i