class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # convert to adj dictionary with source: [destination, weight]
        adj = {}
        for i in range(n): 
            adj[i] = [] 
        
        for s,d,w in edges: 
            adj[s].append([d, w])

        # init (1) result shortest dictionary and (2) min heap [[0, src]]
        shortest = {}
        minHeap = [[0, src]]
        
        # run core loop: add everything to heap, and pop the smallesst one 
        while minHeap: 
            w1, n1 = heapq.heappop(minHeap) 

            if n1 in shortest: 
                continue
            shortest[n1] = w1 

            for n2, w2 in adj[n1]: 
                if n2 not in shortest: 
                    heapq.heappush(minHeap, [w1+w2, n2])
        

        for i in range(n): 
            if i not in shortest: 
                shortest[i] = -1
                
        return shortest


