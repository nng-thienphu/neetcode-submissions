# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # edge case
        if p is None and q is None: 
            return True 
        
        if p is None or q is None:
            return False 

        # base case
        if (p.val != q.val): 
            return False
        # else: # KEY: We cannot do this since 
        #.     False is local. One mismatch anywhere in the tree is enough to say "not the same."
        #.     True is global. To say "yes, the trees are the same," you need every single position to match
        #     return True

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right) 

        return (left and right) 


