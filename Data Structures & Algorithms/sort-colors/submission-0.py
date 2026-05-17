class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0,0,0]
    
        
        # step 1: create count list first, since their element is also their index
        for num in nums: 
            counts[num] += 1
            
        # step 2: n*i -> nums
            # trick using enumerate
            # counts = [2, 1, 1]
            # enumerate yields: (0, 2), then (1, 1), then (2, 1)     
        i = 0              
        for color, count in enumerate(counts): 
            for _ in range(count): 
                nums[i] = color
                i += 1

            