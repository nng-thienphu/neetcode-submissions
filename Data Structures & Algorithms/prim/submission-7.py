class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # create 2 dir adj list from edges
        adj = {}
        for i in range(n): 
            adj[i] = [] 
        for src, dst, w in edges: 
            adj[src].append([dst, w]) 
            adj[dst].append([src, w])

        # init heap and visit set 
        minHeap = [] 
        visit = set()
        visit.add(0)
        for dst, w in adj[0]: 
            heapq.heappush(minHeap, [w, 0, dst])

        totalEdges = 0 

        # run the logic, if heap is not empty just pop the smalless edge 
        # question, why we need to track the length of the visit here
        while minHeap and len(visit) < n: 
            w1, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit: 
                continue
            
            totalEdges += w1 

            visit.add(n2) 
            for neighbor, w2 in adj[n2]: 
                if neighbor in visit: 
                    continue 
                heapq.heappush(minHeap, [w2, n2, neighbor])
        
        return totalEdges if len(visit) == n else -1 

                 
