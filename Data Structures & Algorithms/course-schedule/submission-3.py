class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        indegree = [0] * numCourses 
        for i in range(numCourses): 
            adj[i] = []
        for next_course, prev_course in prerequisites: 
            adj[prev_course].append(next_course)
            indegree[next_course] += 1 
        
        
        q = deque()
        for i in range(numCourses): 
            if indegree[i] == 0: 
                q.append(i) 
        
        res = [] 
        while q: 
            node = q.popleft() 
            res.append(node)
            for neighbor in adj[node]: 
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: 
                    q.append(neighbor) 
        
        if len(res) < numCourses: 
            return False
        
        return True
        

