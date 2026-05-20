class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        result = 0

        for e in nums: 
            arr.append(-e) 
        
        heapq.heapify(arr)

        for i in range(k): 
            result = heapq.heappop(arr)
        
        return -result
        
