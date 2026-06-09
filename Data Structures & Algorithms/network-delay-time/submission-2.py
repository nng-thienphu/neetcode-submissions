class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # KEY STEP 1. Convert edges into adj
        adj = {} 
        for i in range(1, n+1): 
            adj[i] = [] 
        # output: # {1: [], 2: [], 3: [], 4: []}
        
        # s = src, d = dst, w = weight
        for s, d, w in times: 
            adj[s].append([d,w]) 
        # output: {
        #     1: [[2, 5], [3, 2]],   # node 1 → node 2 (cost 5), node 1 → node 3 (cost 2)
        #     2: [[4, 1]],           # node 2 → node 4 (cost 1)
        #     3: [],                 # node 3 has no outgoing edges
        #     4: []                  # node 4 has no outgoing edges
        # }

        # KEY STEP 2: Use min heap to keep the minimum of the current node 
        # The min-heap always hands you the smallest tentative cost in the whole frontier.
        # So when a node pops, nothing cheaper is anywhere in the heap 
        # everything else waiting is ≥ this cost.
        result = {}  # keep shortest path value to each node. Output= {1: 0, 3: 2, 2: 3, 4: 4}
        minHeap = [[0, k]] 
        last = 0 

        while minHeap: 

            # decided which item to pop based on w1;
            w1, n1 = heapq.heappop(minHeap) 

            # already been visted, which mean already find its minimum
            if n1 in result: 
                continue
            result[n1] = w1
            last = w1

            # go to the next node
            for n2, w2 in adj[n1]: 
                if n2 not in result: 
                    heapq.heappush(minHeap, [w1 + w2, n2])

        if len(result) < n: 
            return -1
        else: 
            return last
