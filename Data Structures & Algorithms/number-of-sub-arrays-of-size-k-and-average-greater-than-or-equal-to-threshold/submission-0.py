class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        total = 0
        count = 0
        target = k * threshold

        for r in range(len(arr)):
            total += arr[r]                  # add
            
            if r - l + 1 > k:                # shrink (uses l)
                total -= arr[l]
                l += 1
            
            if r - l + 1 == k:               # check (uses l)
                if total >= target:
                    count += 1

        return count