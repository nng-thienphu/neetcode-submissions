# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return [] 
        
        result = [] 

        def left_boundary(node): 
            if not node or (not node.left and not node.right): 
                return
            result.append(node.val) 
            if node.left: 
                left_boundary(node.left) 
            else: 
                left_boundary(node.right)
            

        def right_boundary(node): 
            if not node or (not node.left and not node.right): 
                return
            
            if node.right: 
                right_boundary(node.right) 
            else: 
                right_boundary(node.left) 
            
            result.append(node.val) 
        
        def leaves(node): 
            if not node:
                return
            if not node.left and not node.right: 
                result.append(node.val) 
                return
            
            leaves(node.left) 
            leaves(node.right) 
        
        result.append(root.val) 
        left_boundary(root.left)
        if root.left or root.right: 
            leaves(root)
        right_boundary(root.right) 
        return result
