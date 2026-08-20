class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # prune 1, the leaf node is the root node, no need to peel 
        if n == 1: 
            return [0]

        indegree = [0] * n 
        adj = {i: [] for i in range(n)}
        for node1, node2 in edges: 
            adj[node1].append(node2) 
            adj[node2].append(node1)
            indegree[node1] += 1 
            indegree[node2] += 1 

        q = deque()
        for i in range(n): 
            if indegree[i] == 1: 
                q.append(i)
        remain = n # total unpeeled nodes, layer count
        
        while remain > 2 :         
            for _ in range(len(q)): 
                node = q.popleft()
                remain -= 1 

                for neighbor in adj[node]: 
                    indegree[neighbor] -= 1 
                    if indegree[neighbor] == 1: 
                        q.append(neighbor) 
        return list(q)