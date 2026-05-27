class Solution:
    # KEY: Shrink from the left while the window is still valid — the early elements that had to be there often become redundant once a bigger element joins from the right.

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0 
        best = float('inf') 

        for r in range(len(nums)): 
            total += nums[r] 
            while total >= target: 
                best = min(best, r-l+1) 
                total -= nums[l]
                l += 1
        
        return best if best != float('inf') else 0