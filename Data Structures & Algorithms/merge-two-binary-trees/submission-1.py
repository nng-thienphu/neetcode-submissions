# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: 
            return root2
        if not root2: 
            return root1
        
        stack = [(root1, root2)] 

        while stack:
            n1, n2 = stack.pop()
            n1.val += n2.val

            # LEFT side
            if n1.left and n2.left: 
                stack.append((n1.left, n2.left))
            elif not n1.left:
                n1.left = n2.left
            
            # RIGHT side
            if n1.right and n2.right: 
                stack.append((n1.right, n2.right))
            elif not n1.right: 
                n1.right = n2.right

        return root1