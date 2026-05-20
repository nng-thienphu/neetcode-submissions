class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [
            (x**2 + y**2, [x, y]) for x, y in points # tuples inside lists
         ]
        heapq.heapify(dist) 

        result = []

        for _ in range(k): 
            result.append(heapq.heappop(dist)[1]) 
        
        return result