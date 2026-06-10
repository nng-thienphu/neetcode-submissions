class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # STEP 1. Create 2-directional ajdency list 
        adj = {} 
        for i in range(0, n): 
            adj[i] = [] 
        
        # KEY: Because this is undirected graph, so we need two direction
        for n1, n2, weight in edges: 
            adj[n1].append([n2, weight]) 
            adj[n2].append([n1, weight]) 
        
        # STEP 2. Initialize minHeap with the first element in adjcency list
        # KEY: minHeap always have the structure of: [weight, src, des]
        minHeap = []
        for neighbor, weight in adj[0]: 
            heapq.heappush(minHeap, [weight, 0, neighbor])
            # output after the 1st element in adj list: [[3, 1, 3], [10, 1, 2]]
            ## the cheapest CROSSING edge (weight sorts first).

        
        # STEP 3. Initilize 2 list 
        # KEY: Create 2 list, one is set for fast checking, one is list for result
        #      Then use minHeap in while
        result = []  # minimum spanning tree list 
        total_weight = 0
        visit = set()
        visit.add(0)

        # KEY: the while len(visit) < n loop assume that the graph was always connected
        # If a graph is disconnected, the minHeap becomes empty. Example: edges=[[0,1,4],[1,2,7]]
        # The minHeap becomes empty before the nodes are visited. 
        while minHeap and len(visit) < n: 
            # STEP 4.1: Pop out the cheapeast edge crossing the boundary
            # and add the second node to the result
            # if the node passed the visit check 
            weight, n1, n2 = heapq.heappop(minHeap) 
            if n2 in visit: 
                continue
            result.append([n1, n2])
            total_weight += weight
            visit.add(n2)

            # STEP 4.2: Go to the next node (neighbor)
            # if the neighbor passed the visit check
            for neighbor, weight in adj[n2]: 
                if neighbor not in visit: 
                    heapq.heappush(minHeap,[weight, n2, neighbor]) # [weight, src, end]
            





        
        return total_weight if len(visit) == n else -1