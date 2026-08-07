class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            adj[src].append(dst)              # prereq -> unlocked course (your direction, correct)

        UNTOUCH, VISITING, VISITED = 0, 1, 2
        state = [UNTOUCH] * numCourses
        result = []

        def dfs(i):
            state[i] = VISITING
            for course in adj[i]:
                if state[course] == VISITING:
                    return True
                if state[course] == UNTOUCH and dfs(course):
                    return True
            state[i] = VISITED
            result.append(i)                  # THE black moment — i is done, everything below it is done
            return False

        for i in range(numCourses):
            if state[i] == UNTOUCH:
                if dfs(i):                    # cycle found -> no valid order exists
                    return []

        return result[::-1]                   # blacks finish leaves-first -> reverse for roots-first