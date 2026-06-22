class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0 
        currSets = []

        def backtracking(i, nums, currSets): 
            nonlocal result 

            # basecase
            if i == len(nums): 
                # XOR all elements in currSets
                xor_total = 0
                for e in currSets: 
                    xor_total = xor_total ^ e 
                
                result += xor_total 
                return 

            currSets.append(nums[i])
            backtracking(i+1, nums, currSets) 

            currSets.pop()
            backtracking(i+1, nums, currSets)

        backtracking(0, nums, currSets) 
        return result 