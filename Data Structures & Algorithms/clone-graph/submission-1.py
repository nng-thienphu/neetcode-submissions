"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # KEY 1: Cannot use list.copy() — we need to create entirely new Node objects,
    #        not just a new list pointing to the original nodes.

    # KEY 2: Solve with BFS.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 0. Edge case: empty graph
        if not node:
            return None

        # 1. Initialize the queue and the clone map
        queue = deque([node])

        clone_map = {node: Node(node.val)}
        # clone_map maps each original node to its clone:
        # {
        #     node1: c1,    # node1 is the input object; c1 is the new Node(val=1) we created
        #     node2: c2,
        #     node3: c3,
        # }

        # 2. BFS through the graph
        while queue:
            # 3. Pop the next node to process
            curr_node = queue.popleft()
            curr_clone = clone_map[curr_node]  # fetch curr's clone once — it doesn't change in the inner loop

            for neighbor in curr_node.neighbors:
                # a. If this neighbor hasn't been seen yet, clone it and enqueue it.
                #    Each node is enqueued exactly once — the moment it's first discovered.
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # b. Wire the edge in the clone graph (do this every time, whether the
                #    neighbor was newly created or already existed):
                #      - curr_clone is the clone of curr_node
                #      - clone_map[neighbor] is the clone of neighbor
                #      - append connects them, mirroring the original edge
                curr_clone.neighbors.append(clone_map[neighbor])

        return clone_map[node]