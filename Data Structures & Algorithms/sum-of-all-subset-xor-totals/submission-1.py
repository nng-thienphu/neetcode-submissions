class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0 
        currSets = []
        result += self.backtracking(0, nums, currSets)

        return result 

    def backtracking(self, i, nums, currSets): 
        # basecase
        if i == len(nums): 
            # XOR all elements in currSets
            xor_total = 0
            for e in currSets: 
                xor_total = xor_total ^ e 
            
            return xor_total 

        currSets.append(nums[i])
        take = self.backtracking(i+1, nums, currSets) 

        currSets.pop()
        skip = self.backtracking(i+1, nums, currSets)

        return take + skip