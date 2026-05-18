# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # KEY: They key to solve this problem is to remind yourself that
    #.     inorder traversal already sort all the node 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(root): 
            if root is None:
                return 
            # KEY: when reach to the leaf NULLL node
            #.     then it will skip the return go straight
            #.     the line of adding the root value into the array 
            left = inorder(root.left)
            arr.append(root.val)
            right = inorder(root.right)
        
        inorder(root)
        return arr[k-1]