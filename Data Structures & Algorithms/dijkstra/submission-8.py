class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {} 
        for i in range(n): 
            adj[i] = []
        for sc, dst, w in edges: 
            adj[sc].append([dst, w])
        
        minHeap = [] 
        for neighbor, weight in adj[src]: 
            heapq.heappush(minHeap, [weight, src, neighbor]) 
        
        minCost = {}
        minCost[src] = 0 
        
        while minHeap: 
            w1, n1, n2 = heapq.heappop(minHeap)  
            if n2 in minCost: 
                continue
            
            minCost[n2] = w1 

            for neighbor, w2 in adj[n2]: 
                heapq.heappush(minHeap, [w2 + w1, n2, neighbor])
            
        for i in range(n): 
            if i not in minCost: 
                minCost[i] = -1
        
        return minCost


