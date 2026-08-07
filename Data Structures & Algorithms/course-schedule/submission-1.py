class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] 

        for a, b in prerequisites: 
            graph[b].append(a) 
        
        # graph = [[1, 2], [3], [3], []]   
        # means that, 0 unlocks 1 and 2; 1 unlocks 3; 2 unlocks 3

        UNTOUCH = 0
        VISITING = 1 
        VISITED = 2 
        state = [UNTOUCH] * numCourses

        def dfs(u): 
            state[u] = VISITING

            for v in graph[u]: 
                if state[v] == VISITING: 
                    return True 
                if state[v] == UNTOUCH and dfs(v): 
                    return True
            
            state[u] = VISITED

            return False
        

        cycle_found = False
        for i in range(numCourses):  # try every course as a starting point
            if state[i] == UNTOUCH:  # only start from WHITE (untouched) courses;
            # visited ones were already certified by an earlier dfs
                if dfs(i): 
                    cycle_found = True 
                    break
        return False if cycle_found else True






        

