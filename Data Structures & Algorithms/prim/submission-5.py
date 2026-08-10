class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {} 
        for i in range(0, n): 
            adj[i] = [] 
        for src, dst, w in edges: 
            adj[src].append([dst, w]) 
            adj[dst].append([src, w]) 
        
        minHeap = [] 
        for neighbor, w in adj[0]: 
            heapq.heappush(minHeap, [w, 0, neighbor]) 
        
        visit = set()
        visit.add(0)
        globalMin = 0 

        while minHeap and len(visit) < n: 
            w1, n1, n2 = heapq.heappop(minHeap) 

            if n2 in visit: 
                continue
            globalMin += w1 
            visit.add(n2)

            for neighbor, w2 in adj[n2]:  
                if neighbor not in visit: 
                    heapq.heappush(minHeap, [w2, n2, neighbor]) 
        
        return globalMin if len(visit) == n else -1 

            
            

        