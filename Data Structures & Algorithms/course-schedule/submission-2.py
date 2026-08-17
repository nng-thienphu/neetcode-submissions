class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {} 
        for i in range(numCourses): 
            adj[i] = [] 
        for dst, src in prerequisites: 
            adj[src].append(dst)
        
        result = []
        visited = set()
        path = set()

        def cycle_detection(src): 
            if src in path: 
                return True
            if src in visited: 
                return False

            path.add(src) 
            for neighbor in adj[src] : 
                if cycle_detection(neighbor): 
                    return True
            
            path.remove(src) 
            visited.add(src) 
            result.append(src) 

            return False
        
        for i in range(numCourses): 
            if cycle_detection(i): 
                return False
        
        return True