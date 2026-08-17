class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k *  threshold
        windowSum = 0 
        count = 0
        L = 0

        for R in range(len(arr)): 
            windowSum += arr[R]

            if R - L + 1 > k: 
                windowSum -= arr[L] 
                L += 1 
            if R - L + 1 == k and windowSum >= target: 
                count += 1 
            
        return count 
            
