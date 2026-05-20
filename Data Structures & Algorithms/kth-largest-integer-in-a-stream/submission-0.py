class KthLargest:
    # They key of this is that whenever you want to pop 
    #.    the pop only remove the smallest number in array of k-largest number
    #.       -> using heap for the k-largest number is the best
    #.                since you don't need to sorted or anything, 
    #.                just care about the smallest number

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] 
        for num in nums: 
            self.add(num) 

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) 
        if len(self.heap) > self.k :
            heapq.heappop(self.heap) 
        return self.heap[0] 