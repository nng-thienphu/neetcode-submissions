class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {} 
        indegree = [0] * n 
        for i in range(n): 
            adj[i] = []
        for u, v in edges: 
            adj[u].append(v) 
            indegree[v] += 1 
        
        q = deque()
        for i in range(n): 
            if indegree[i] == 0: 
                q.append(i)

        result = []
        while q: 
            node = q.popleft()
            result.append(node)

            for neighbor in adj[node]: 
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: 
                    q.append(neighbor) 

        if len(result) < n: 
            return [] 

        return result
                
