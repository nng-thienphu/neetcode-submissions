class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(i, remaining, path):
            # success: hit target exactly
            if remaining == 0:
                output.append(path[:])      # append a *copy* — path keeps mutating
                return
            
            # failure: ran out of numbers to consider
            if i == len(nums):
                return
            
            # try every valid number of copies of nums[i]
            max_copies = remaining // nums[i]
            for copies in range(0, max_copies + 1):
                # add `copies` of nums[i] to path
                for _ in range(copies):
                    path.append(nums[i])
                
                # recurse to next index with updated remaining
                backtrack(i + 1, remaining - copies * nums[i], path)
                
                # undo: remove the `copies` we just added
                for _ in range(copies):
                    path.pop()
        
        backtrack(0, target, [])
        return output