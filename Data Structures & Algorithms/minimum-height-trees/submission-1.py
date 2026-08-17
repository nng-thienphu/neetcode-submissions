class Solution:
    # KEY INSIGHTS: a node survives k rounds ⟺ its distance to the farthest leaf is (roughly) k. 
    # => peeling from outside (leaf nodes) to inside
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]: 
        if n==1: 
            return [0] 

        adj = {} 
        indegree = [0]*n
        for i in range(n): 
            adj[i] = []
        for src, dst in edges: 
            adj[src].append(dst) 
            indegree[src] += 1

            adj[dst].append(src) 
            indegree[dst] += 1
        
        q = deque()
        for i in range(n):  # leaf node is the node has indegree of 1
            if indegree[i] == 1: 
                q.append(i) 
        
        while q: 
            # A path's middle is either 1 node (odd length) 
            # or 2 adjacent nodes (even length), 
            # never 3 — so the centers of a tree, which are the middle of its longest path 
            if n <= 2: 
                return list(q) 
            for _ in range(len(q)): 
                node = q.popleft()
                n -= 1
                for neighbor in adj[node]: 
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        q.append(neighbor)
            

            
            


        
        
        

        

        