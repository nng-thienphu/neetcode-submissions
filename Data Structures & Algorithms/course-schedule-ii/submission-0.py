class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # convert into adj list
        adj = {} 
        for i in range(numCourses): 
            adj[i] = []
        for course in prerequisites:  
            adj[course[0]].append(course[1])

        # init with visited and path tracking
        visited = set()
        path = set()
        result = []

        # code dfs function
        def dfs(course): 
            # check if visited
            if course in visited: 
                return True

            # check cycle detection
            if course in path: 
                return False

            path.add(course)

            # recurse all of the children
            for children in adj[course]: 
                if not dfs(children): 
                    return False 
            
            path.remove(course)
            visited.add(course) 
            result.append(course)
            return True

        # apply dfs to every node to reach its children
        for i in range(numCourses): 
            if not dfs(i):
                return []

        # return the revert result
        # result.reverse()
        return result