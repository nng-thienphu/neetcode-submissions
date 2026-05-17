# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # To check at every node, run recursive.
        #.  We need to check 2 things at every node:
        #.  (1) height
        #.  (2) balance check

        # Algorithm 1: finding the height at one node
        # the trick to solve this problem is applying max() function to traversal algorithm
        #.   since the path from this node to its deepest leaf
        #.   goes through one of its children (the deeper one).
        #.   So we need to pick the deeper child with max, then add 1
        #.   equivalent to 1 + max(left_h, right_h)
        #.   run recursive at every node

        # Algorithm 2: Constantly checking the balance at every node
        #.   Balance must hold at every node, not just the root — so the check itself has to recurse down the tree.
        #.   isBalanced calls itself on left and right children, so every node gets checked.

        def height(root): 
            # base case
            if root is None:
                return 0
            
            # recursive in height 
            left = height(root.left) 
            right = height(root.right) 
            return max(left, right) + 1
        
        # edge case, empty tree
        if root is None:
            return True


        # height check
        right = height(root.right)
        left = height(root.left) 
        if abs(left - right) > 1: 
            return False 
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

