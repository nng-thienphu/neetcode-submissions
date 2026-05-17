from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k = 1
        high_k = max(piles)

        while low_k <= high_k:
            mid_k = (low_k + high_k) // 2
            hours_mid = self.total_hours(piles, mid_k)

            if hours_mid > h:          # ❌ too slow — eat faster
                low_k = mid_k + 1
            else:                      # ✅ fits — try slower
                high_k = mid_k - 1

        return low_k

    def total_hours(self, piles, guess_k):
        total = 0
        for banana in piles:
            total += ceil(banana / guess_k)
        return total