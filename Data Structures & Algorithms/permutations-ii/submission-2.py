class Solution:
    # KEY INSIGHT FOR THE PERMUTATION 
    # knob 3, we take all the elemtn, filter by the one has not used yet
    # knob 2, the length if the length of the state the same with lenght of the original array
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        n = len(nums)
        used = [False] * n
        nums.sort() 

        def backtrack(path): 
            if len(path) == n: 
                res.append(path.copy()) 
                return
            
            for i in range(n): 
                if used[i] == True: 
                    continue
                
                if i > 0 and nums[i-1] == nums[i] and not used[i-1]: 
                    continue 
                
                used[i] = True
                path.append(nums[i]) 
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res