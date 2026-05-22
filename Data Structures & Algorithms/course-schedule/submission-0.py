class Solution:
    # METHOD: BFS 
    # KEY: Use in-degree as how many prerequisites the course is still waiting on. 
    #.     When that number is 0, the course's checklist is empty, so it's ready to take

    # STATE: 
    # in-degree[c] = number of prerequisites course c is still waiting
    # graph[c] = list of courses that depend on c 
    # Take a course when its in-degree hits 0.
    # Taking it triggers decrements down the chain.

    # CODE MANIFESTATION: 
    # 1. decrement dependent's in-degree
    # 2. if it just hit 0, enqueue it

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # set-up: turning edge list -> graph list 
        in_degree = [0] * numCourses 
        graph = [[] for _ in range(numCourses)] 

        for course, pre in prerequisites:    
            graph[pre].append(course)
            in_degree[course] += 1
        
        # seed: create queue + find 1st course without preq
        queue = deque() 
        for i in range(len(in_degree)): 
            if in_degree[i] == 0: 
                queue.append(i)
        
        # run BFS
        course_taken = 0
        while queue: 
            pre = queue.popleft() 
            course_taken += 1 

            for course in graph[pre]: 
                in_degree[course] -= 1 
                if in_degree[course] == 0: 
                    queue.append(course) 
            
        return course_taken == numCourses



        
