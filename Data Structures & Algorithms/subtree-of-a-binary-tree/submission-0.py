# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True
        if not root: 
            return False
        
        if self.isSame(root, subRoot): 
            return True 
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

    def isSame(self, m, n):
        if not m and not n: 
            return True
        
        if not m or not n: 
            return False
        
        if m.val != n.val: 
            return False
        
        return self.isSame(m.left, n.left) and self.isSame(m.right, n.right)


