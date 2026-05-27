class Solution:
    # WRONG ASSUMPTION: 
    # I tried comparing nums[r] to nums[r-1] and nums[r-2] to spot duplicates. That worked in the last problem. It breaks here because you also write into the front of the array. So nums[r-1] might be a value you just overwrote, not the original. The lookback lies to you.

    # KEY INSIGHT: 
    # The array is sorted. So equal values sit in a run next to each other.
    # For each run, you keep at most 2 copies:

    # Run of length 1 → write 1 copy at the left
    # Run of length 2+ → write 2 copies at the left 


    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 1

        while r <= len(nums)-1: 
            if r < len(nums) - 1 and nums[r] == nums[r+1]:
                count += 1

            else: 
                if count >= 2: 
                    for i in range(2):  
                        nums[l] = nums[r]
                        l += 1 
                else: 
                    nums[l] = nums[r]
                    l+= 1 
                
                count = 1 

            r += 1 
        return l    