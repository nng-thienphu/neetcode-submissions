class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        seen = {0: 1}              # prefix sum 0 occurs once: the empty prefix

        for num in nums:
            prefixSum += num
            count += seen.get(prefixSum - k, 0)   # how many earlier prefixes complete a k-sum?
            seen[prefixSum] = seen.get(prefixSum, 0) + 1

        return count