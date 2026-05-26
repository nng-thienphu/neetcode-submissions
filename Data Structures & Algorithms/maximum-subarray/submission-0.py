class Solution:
    # My Wrong throught: 
    # I thought we can just run best = max(current_element, current_element + next_element) 
    # but this is wrong approach because it can only handle the sub array starting from the first element

    # KEY: How to actually seperate the subarray in the middle is the hard part
    #      At one point, we will have to decide to extend the run, or restart from nums[i]. 
    #      code technique: curr = max(nums[i], curr + nums[i])
    #           - If nums[i] alone is bigger → curr becomes nums[i] → that's "restart."
    #.          - If curr + nums[i] is bigger → curr keeps growing the run → that's "extend."
    #         => basically, the algebra: curr + nums[i] > nums[i] simplifies to curr > 0 
    

    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        
        return best
        
        