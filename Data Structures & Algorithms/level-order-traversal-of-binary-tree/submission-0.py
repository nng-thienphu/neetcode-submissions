# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # KEY: To solve this problem, we need to implement double ended queue
    #       so that we can remmber to go trhough 2 child node of each parent node
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case, if the list is empty
        if not root : 
            return []

        result = [] 

        queue = deque([root]) 

        while queue: 
            level_size = len(queue) 
            current_level = [] 
            
            # each node will contains 2 child node (null = pass but still consider)
            #.    this loop will procceed every node in the current level, pushing each node's children
            #           onto the queue for the next level.
            for _ in range(level_size): 
                node = queue.popleft() # pop from the left / first in
                current_level.append(node.val) 

                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
                
            result.append(current_level)

        return result 