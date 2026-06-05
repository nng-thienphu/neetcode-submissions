class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        best = 0
        res = 0 

        for num in nums: 
            counts[num] = counts.setdefault(num, 0) + 1
            if counts[num] > best: 
                res = num 
                best = counts[num]
        
        return res