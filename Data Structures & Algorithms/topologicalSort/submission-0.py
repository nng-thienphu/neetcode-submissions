class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # STEP 1. Convert edges list into adjacency list
        adj = {} 
        for i in range(0, n): 
            adj[i] = []
        for src, dst in edges: 
            adj[src].append(dst) 
        
        # STEP 2. Initialize result list and visit hashset, optional path set (path is for cycle detection only)
        resultTopSort = []    # KEY: this
        visit = set()
        path = set()

        # STEP 3. KEY CODE TECHNIQUE: The graph might not be fully connected
        # If you only called dfs from node 1, 
        # you'd only visit nodes reachable from 1. 
        # Any isolated node or separate component would be missed.
        for i in range(n): 
            self.dfs(i, adj, visit, path, resultTopSort) 

        resultTopSort.reverse()
        return resultTopSort

    def dfs(self, src, adj, visit, path, topSort):    
        # STEP 0. Cycle detection
        if src in path: 
            return False

        # STEP 1. Check if the src already visited, then skip entirely
        if src in visit: 
            return True

        # if not visited, then mark it, and run
        visit.add(src)
        path.add(src)

        # STEP 2. go to the neighbor of neighbor
        # This piece of code is KEY to the algorithm
        for neighbor in adj[src]: 
            if self.dfs(neighbor, adj, visit, path, topSort) == False:
                return False  # ← bubble cycle detection up

        path.remove(src)      # ← KEY: leaving src, remove from current path
        topSort.append(src)


