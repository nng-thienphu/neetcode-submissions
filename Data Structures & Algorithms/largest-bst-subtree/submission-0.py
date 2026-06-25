# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        global_size = 0 

        def dfs(node): 
            nonlocal global_size
            # base case
            if not node: 
                # valid BST, min value, max value, size of subtree
                return (True, float('inf'), float('-inf'), 0)
            
            left_valid, left_min, left_max, left_size = dfs(node.left) 
            right_valid, right_min, right_max, right_size = dfs(node.right) 

            if left_valid and right_valid and left_max < node.val < right_min:
                global_size = max(global_size, left_size + right_size + 1)
                return (True, min(left_min, node.val), max(right_max, node.val), left_size + right_size + 1)
            else: 
                global_size = max(global_size, left_size, right_size)
                return (False, float('inf'), float('-inf'), 0)
        dfs(root)
        return global_size