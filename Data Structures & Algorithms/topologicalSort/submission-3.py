class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {} 
        for i in range(n): 
            adj[i] = [] 
        for src, dst in edges: 
            adj[src].append(dst) 

        topResult = []
        visited = set()
        path = set() 

        def dfs(src): 
            if src in visited: 
                return True
            if src in path: 
                return False
            
            path.add(src)
            for neighbor in adj[src]: 
                if not dfs(neighbor): 
                    return False 
            path.remove(src) 

            visited.add(src)
            topResult.append(src)
            return True
        
        for i in range(n): 
            if not dfs(i): 
                return [] 
        
        return topResult[::-1] 