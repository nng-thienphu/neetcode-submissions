# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # edge case: 
        if not root: 
            return []

        queue = deque()
        queue.append(root) 
        
        result = [] 
        result.append(root.val)

        while len(queue) > 0 : 
            for i in range(len(queue)): 
                root = queue.popleft()
                if root.left: 
                    queue.append(root.left)
                if root.right: 
                    queue.append(root.right)
            if queue:
                result.append(queue[-1].val) 
        
        return result 
            
            

                
                