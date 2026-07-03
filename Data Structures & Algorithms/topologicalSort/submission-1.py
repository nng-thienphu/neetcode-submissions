class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        # STEP 1. Convert edges list into adjacency list
        adj = {}  # {1: [2, 3]}
        for i in range(0, n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)

        # STEP 2. Initialize result list, visited set, and path set
        # (path is for cycle detection only)
        resultTopSort = []   # KEY: only holds FINISHED nodes, in post-order
        visited = set()      # PERMANENT memory: "have I ever fully processed this node?"
        path = set()         # TEMPORARY, live: "is this node currently my ancestor
                              #  on the active call stack right now?"

        def dfs(src):
            # STEP 0. ORDER MATTERS: check path (danger) BEFORE visited (comfort)
            # path ⊆ visited in general, but here they're mutually exclusive by
            # design (visited only gets added AFTER path releases the node), so
            # in THIS version the order is actually safe either way — but we
            # keep path-first as the correct habit, since it's the more specific
            # / more dangerous condition.
            if src in visited:
                return True   # repeated node detection: already fully explored, safe to skip

            if src in path:
                return False  # cycle detection: src is still OPEN, an active ancestor
                              # of itself → circular dependency → no valid order exists

            # STEP 1. Enter src: mark it as "currently open" on this branch
            path.add(src)

            # STEP 2. KEY CODE TECHNIQUE: go finish ALL children before touching src
            # A node can only be added to the result once EVERY node it depends on
            # (its neighbors, recursively) has been fully explored and returned True.
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False  # bubble the cycle detection up, don't keep exploring

            # STEP 3. src's entire subtree is done — leaving this branch now.
            # visited only gets a node added the moment that node's entire subtree
            # (all its neighbors, recursively) has been fully explored and returned
            # successfully. path and visited never overlap in time in this version.
            path.remove(src)     # no longer an "open ancestor"
            visited.add(src)     # permanently done, safe forever
            resultTopSort.append(src)  # post-order: add src only AFTER all its children

            return True  # no cycle found in this subtree

        # STEP 4. The graph might not be fully connected — outer loop tries every
        # node as a possible starting root, so disconnected components (or nodes
        # unreachable from node 0) still get visited. Most calls will be no-ops
        # because `visited` already caught that node inside an earlier call's subtree.
        for i in range(n):
            if not dfs(i):
                return []  # cycle found anywhere → no valid ordering exists

        # STEP 5. We appended nodes in "finished" order (deepest dependency first),
        # so the list is backwards — reverse it to get true prerequisite order.
        resultTopSort.reverse()
        return resultTopSort