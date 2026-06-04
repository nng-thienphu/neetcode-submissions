class Solution:

    # KEY 1: Need a padding of 0 at the beginning of the prefix sum array

    # KEY 2: target = prefix_sum[right] - prefix[left]
    #.       => prefix[left] = prefix_sum[right] - target
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = {0: 1} # key = prefix_sum, value = counts

        current_sum = 0
        result = 0
        for i in range(len(nums)) : 
            current_sum += nums[i]
            remain = current_sum - k   

            if remain in prefix_dict: 
                result += prefix_dict[remain] 
            
            # update the current sum -> to prefix sum dictionary 
            prefix_dict[current_sum] = prefix_dict.get(current_sum, 0) + 1 
        
        return result 

