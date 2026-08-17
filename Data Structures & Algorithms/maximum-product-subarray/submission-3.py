class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        currMin, currMax = 1, 1 

        for num in nums: 
            prevMax, prevMin = currMax, currMin
            currMax = max(num * prevMax, num * prevMin, num)
            currMin = min(num * prevMax, num * prevMin, num) 
            res = max(res, currMax) 
        
        return res 