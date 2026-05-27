class Solution:
    # WRONG ASSUMPTION: 
    # I tried comparing nums[r] to nums[r-1] and nums[r-2] to spot duplicates. That worked in the last problem. It breaks here because you also write into the front of the array. So nums[r-1] might be a value you just overwrote, not the original. The lookback lies to you.

    # KEY INSIGHT: 
    # The array is sorted. So equal values sit in a run next to each other.
    # For each run, you keep at most 2 copies:

    # Run of length 1 → write 1 copy at the left
    # Run of length 2+ → write 2 copies at the left 

    def removeDuplicates(self, nums: List[int]) -> int:
        # l = write pointer: where the next kept value goes.
        # r = scan pointer: walks through every index once.
        # count = length of the run we're currently tracking.
        #         starts at 1 because nums[r] itself counts as one.
        l, r = 0, 0
        count = 1

        while r <= len(nums) - 1:
            # Two conditions, fused with `and` (short-circuit):
            #   1. r < len(nums) - 1  → guard so nums[r+1] is safe to access.
            #   2. nums[r] == nums[r+1] → the run continues into the next index.
            # If r is at the last index, condition 1 fails, Python short-circuits,
            # and we fall into the else branch to flush the final run.
            if r < len(nums) - 1 and nums[r] == nums[r+1]:
                count += 1
            else:
                # The run ending at index r is done. Flush it.
                # Write min(count, 2) copies of nums[r] to the front.
                if count >= 2:
                    # Run has 2 or more elements → keep exactly 2 copies.
                    for _ in range(2):
                        nums[l] = nums[r]
                        l += 1
                else:
                    # Run has length 1 → keep 1 copy.
                    nums[l] = nums[r]
                    l += 1
                # Reset for the next run, which will start at r+1.
                count = 1

            r += 1

        # l now points one past the last written index → it equals k.
        return l
