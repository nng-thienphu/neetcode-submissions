class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = [] 

        def backtracking(i, path, total): 
            # basecase 1: hit target
            if total == target: 
                result.append(path.copy()) 
                return
            
            # basecase 2: overshot or out of numbers
            if total > target or i >= len(candidates): 
                return
            
            # INCLUDE candidates[i] 
            path.append(candidates[i]) 
            backtracking(i+1, path, total + candidates[i])
            path.pop() 
                
            # EXCLUDE candidates[i]
            j = i 
            while j < len(candidates) and candidates[j] == candidates[i]: 
                j += 1
            backtracking(j, path, total)
        
        backtracking(0, [], 0) 
        return result 
