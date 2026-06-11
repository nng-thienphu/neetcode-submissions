# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # I have to run for the whole tree  
        # since there is no node that has greate value in between
        # this is preorder traversal 
        # tracking the value in the middle, min current value 
        count = 0

        def preorder(node, biggest): 
            nonlocal count 

            if not node: 
                return

            if biggest <= node.val: 
                print(f"biggest: {biggest}, val:{node.val}")
                biggest = node.val
                count += 1 

            preorder(node.left, biggest) 
            preorder(node.right, biggest) 

        preorder(root, -101) 
        return count 