class Solution:
    # KEY: how to solve this problem is using the rule
    # largest + smallest > target -> decrease the largerst
    # largest + smallest < target -> increase the smallest 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1 

        while l <= r: 
            # print(f"left: {l, numbers[l]}, right: {r, numbers[r]}")
            if numbers[l] + numbers[r] > target: 
                r -= 1 
            elif numbers[l] + numbers [r] < target: 
                l += 1 
            else: 
                return [l+1, r+1] 
        