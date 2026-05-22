"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # KEY 1: Cannot just use list.copy() since we need to create
    #.      entirely new node objects 

    # KEY 2: Using BFS method
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 1. init (1) queue (2) clone map
        queue = deque()
        queue.append(node)

        clone_map = {} 
        # clone_map = {
            #     node1: c1,    # node1 is the input object, c1 is the new Node(val=1) we made 
            #     node2: c2,
            #     node3: c3,
            # }
        if not node: 
            return 
            
        clone_node_1 = Node(node.val)
        clone_map[node] = clone_node_1 

        # 2. run while loop 
        while queue: 
            # 3. move layer by layer
            # don't really need this but add as a standard way for BFS layer-by-layer moving
            size = len(queue) 
            for _ in range(size): 
                # 4. pop left from queue
                curr_node = queue.popleft()
                for neighbor in curr_node.neighbors : 
                    # a. edge case check
                    if neighbor not in clone_map: 
                        new_node = Node(neighbor.val)
                        clone_map[neighbor] = new_node 
                        #b. add to the queue: 
                        # every node goes on the queue exactly once, at the moment it's first discovered.
                        queue.append(neighbor)        

                    # connect new node together in clone map
                    curr_clone = clone_map[curr_node] # 1. fetch the clone of curr 
                    neighbor_clone = clone_map[neighbor] # 2. fetch the clone of neighbor
                    curr_clone.neighbors.append(neighbor_clone) # 3. wire them together 

        return clone_map[node]

