class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums: 
            counts[num] = counts.setdefault(num, 0) + 1
        
        return max(counts, key=counts.get)