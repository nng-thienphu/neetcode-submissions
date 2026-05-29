class Solution:
    # method 1: create two prefix sum array 
    # WRONG ASSUMPTION: 
    # I thought your two prefix arrays were symmetric — that left_prefix[i] and right_prefix[i] both mean "sum on that side of index i." They don't. Trace what each actually contains for nums = [1,7,3,6,5,6]:

    # left_prefix[i] = sum of nums[0..i-1] (excludes nums[i]) ✓
    # right_prefix[i] = sum of nums[i..n-1] (includes nums[i]) ✗
            # -> right prefix need to [i+1] to exclude the nums[i]


    def pivotIndex(self, nums: List[int]) -> int:
        right_prefix = self.helper_right_prefix(nums) 
        left_prefix = self.helper_left_prefix(nums)
        print(left_prefix)
        print(right_prefix)

        for i in range(len(nums)): 
            if left_prefix[i] == right_prefix[i+1] : # right[i+1]
                print(right_prefix[i+1])
                return i
        return -1 

    
    def helper_left_prefix(self, nums): # return a list of prefix from left to right  
        total = [] 
        total.append(0)
        current_sum = 0
        
        for i in range(len(nums)): 
            current_sum += nums[i]
            total.append(current_sum)
        
        return total
    
    def helper_right_prefix(self, nums): # return a list of prefix from right to left
        total = []
        total.append(0)

        current_sum = 0

        for i in reversed(range(len(nums))): 
            current_sum += nums[i]
            total.append(current_sum)
        
        return total[::-1]