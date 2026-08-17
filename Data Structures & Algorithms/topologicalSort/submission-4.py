class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build the graph AND count incoming edges for each vertex
        adj = {}
        indegree = [0] * n                 # indegree[v] = how many edges point INTO v
        for i in range(n): 
            adj[i] = [] 
        for u, v in edges:
            adj[u].append(v)
            indegree[v] = indegree[v] + 1  # v gained one incoming edge

        # Start with every vertex that has NO prerequisites (indegree 0)
        queue = deque()
        for vertex in range(n):
            if indegree[vertex] == 0:
                queue.append(vertex)

        order = []
        while queue:
            u = queue.popleft()
            order.append(u)                # u has no remaining prerequisites → safe to place

            # "Remove" u from the graph: every neighbor loses one incoming edge
            for v in adj[u]:
                indegree[v] = indegree[v] - 1
                if indegree[v] == 0:       # v's last prerequisite just got placed
                    queue.append(v)

        # Cycle check: if some vertices never reached indegree 0,
        # they're stuck in a cycle and never entered the order
        if len(order) < n:
            return []

        return order