class Solution:
    # WRONG ASSUMPTION:
    # probability of 2 node is the sum
    # no, we have to multiply not summing any shit. 
    # The graph is undirected — you're only adding the edge s → d but not d → s. You need to add both directions.
    # Probability multiplication with negatives — you're storing -p in the adjacency list, but then doing p1 * p2 where p1 is already negative. Multiplying two negatives gives a positive, which breaks the heap ordering.
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # step 1. convert edge into adjacency list
        adj = {}
        for i in range(n): 
            adj[i] = [] # {source: [destination, probability] } 

        idx = 0 
        while idx < len(edges): 
            s = edges[idx][0]
            d = edges[idx][1]
            p = succProb[idx] 

            adj[s].append([d, p]) 
            adj[d].append([s, p])
            idx += 1  
        
        
        # step 2. use max-heap to pull the closest node with higest prob
        longest = {}   # {1: 0, 2: -0.25, 3: -0.5}
        minHeap = [[-1, start_node]] # weight need to be first

        while minHeap: 
            p1, n1 = heapq.heappop(minHeap) 

            if n1 in longest: 
                continue
            longest[n1] = p1

            for n2, p2 in adj[n1]: 
                if n2 not in longest: 
                    heapq.heappush(minHeap, [(p1*p2), n2])
        
        return -longest.get(end_node, 0)