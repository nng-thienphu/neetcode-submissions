class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        target = threshold * k 
        L = 0 
        count = 0 
        windowSum = 0 

        for R in range(n):
            windowSum += arr[R] 

            if R-L+1 > k: 
                windowSum -= arr[L]
                L += 1 
            if R-L+1 == k and windowSum >= target: 
                count += 1 
        
        return count 