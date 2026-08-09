class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # create 2 dir adj list
        adj = {} 
        for i in range(n): 
            adj[i] = [] 
        for s,d,w in edges: 
            adj[s].append([d,w]) 
            adj[d].append([s,w]) 

        # init (1) visit set and (2) minHeap with the first element in it
        minHeap = []
        for neighbor, weight in adj[0]: 
            heapq.heappush(minHeap, [weight, 0, neighbor]) 
        visit = set()
        visit.add(0) 
        
        # core logic, loop through the node 
        result = []
        total_weight = 0 

        while minHeap and len(visit) < n: 
            # 1. pop out the smallest of weight, source, destination in the min Heap
            weight, n1, n2 = heapq.heappop(minHeap) 
            if n2 in visit: 
                continue
            
            # 2. add up the total weight 
            total_weight += weight 
            visit.add(n2)

            # 3. loop through every neighbor in n2 since n2 not visited yet
            for neighbor, weight in adj[n2]: 
                if neighbor not in visit: 
                    heapq.heappush(minHeap, [weight, n2, neighbor]) 
            
        return total_weight if len(visit)==n else -1

        

        