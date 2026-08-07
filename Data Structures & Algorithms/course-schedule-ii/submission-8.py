class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adj list
        adj = [[] for _ in range(numCourses)] 
        for dst,src in prerequisites: 
            adj[src].append(dst) 

        # state list
        UNTOUCH = 0
        VISITING = 1 
        VISITED = 2
        state = [UNTOUCH] * numCourses

        # init result list
        result = [] 

        # dfs function
        def dfs(i): 
            state[i] = VISITING

            for course in adj[i]: 
                if state[course] == VISITING: 
                    return True 

                if state[course] == UNTOUCH and dfs(course): 
                    return True 
            result.append(i)
            state[i] = VISITED 
            return False 

        # implement and return reverse order 
        for i in range(numCourses): 
            if state[i] == UNTOUCH: 
                if dfs(i): 
                    return [] 
        
        return result[::-1]
