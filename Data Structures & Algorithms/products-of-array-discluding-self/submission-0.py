class Solution:
    # WRONG ASSUMPTION: 
    # My original approach computed the total product and divided by each element. 
    # But division breaks on zeros and the follow-up forbids it anyway 

    # KEY 1: INSIGHTS
    # the answer at index i is (product of everything to its left) × (product of everything to its right)
    # this approach lets you avoid division entirely

    # KEY 2: CODE
    # In both passes, store the running product into result[i] before multiplying nums[i] into it
    # storing after wrongly includes nums[i] itself in its own answer. 
    # And in the second pass, multiply into result[i] (*=), don't assign (=) — assigning overwrites the left products from pass 1 instead of combining left × right. 
    # Rule of thumb: write first, then update the running variable. 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        left = 1 
        for i in range(len(nums)): 
            result[i] = left 
            left *= nums[i] 

        right = 1
        for i in range(len(nums)-1, -1, -1): 
            result[i] *= right
            right *= nums[i]
        
        return result 