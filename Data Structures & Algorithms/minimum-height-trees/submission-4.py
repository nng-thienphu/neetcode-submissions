class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # single node: it is its own root
        if n == 1:
            return [0]

        # undirected tree: adjacency + degree count
        degree = [0] * n
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1

        # seed with current leaves
        q = deque(i for i in range(n) if degree[i] == 1)

        # peel leaves layer by layer; centers are the last 1-2 survivors
        remain = n
        while remain > 2:
            # full layer per round: stop-check only between generations
            for _ in range(len(q)):
                node = q.popleft()
                remain -= 1
                for neighbor in adj[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        q.append(neighbor)

        return list(q)