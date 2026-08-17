class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses): 
            adj[i] = []
        for next_course, prev_course in prerequisites: 
            adj[next_course].append(prev_course)
        
        
        visited = set()
        path = set() 
        result = [] 

        def dfs(i): 
            if i in visited: 
                return True
            if i in path: 
                return False 
            
            path.add(i) 
            for neighbor in adj[i]:
                if not dfs(neighbor):
                    return False 
            path.remove(i)
            visited.add(i)
            # append only the path has already done
            result.append(i)  
            return True

        
        for i in range(numCourses): 
            if not dfs(i): 
                return []
        return result
        


                

