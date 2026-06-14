class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, curr_xor): 
            if index == len(nums): 
                return curr_xor
            
            take = backtrack(index + 1, curr_xor ^ nums[index]) 
            skip = backtrack(index +1, curr_xor)

            return take + skip 
        
        return backtrack(0, 0)