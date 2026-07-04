class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # convert edges into adj list
        adj = {}
        for i in range(n): 
            adj[i] = [] 
        for src, dst in edges: 
            adj[src].append(dst) 

        # init visited and path set
        visited = set()
        path = set()
        resultReverse = [] 

        # dfs function
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
            resultReverse.append(src)
            return True

        # apply dfs to each node 
        for i in range(n):
            if not dfs(i): 
                return []

        # return reversed result
        resultReverse.reverse()
        return resultReverse