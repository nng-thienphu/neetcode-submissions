class Solution:
    # KEY: Python only gives you a min-heap
    #.     use negative sign -> Push -stone instead of stone
    #.     A min-heap of negatives behaves exactly like a max-heap of positives.
    def lastStoneWeight(self, stones: List[int]) -> int:
        # initialize a heap 
        arr = [-e for e in stones] 
        heapq.heapify(arr)
        
        # run the logic
        while len(arr) > 1: 
            x = heapq.heappop(arr)  # -13
            y = heapq.heappop(arr)  # -12 

            if x == y: 
                pass
            else:
                x = x - y
                heapq.heappush(arr, x)
            

        return -arr[0] if arr else 0 


        