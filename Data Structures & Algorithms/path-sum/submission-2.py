# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # METHOD: Depth-First Search
    #
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Edge case: empty tree has no root-to-leaf path.
        if not root:
            return False
        
        return self.dfs(root, 0, targetSum)

    
    def dfs(self, node, current_sum, targetSum): 
        # base case 1: 
        #.   we don't have to return the path so True, False is enough
        if not node: 
            return False
        
        # base case 2: a leaf has no left child and no right child
        if not node.left and not node.right : 
            if current_sum + node.val == targetSum:
                return True
            else: 
                return False

        # recursive call 
        left = self.dfs(node.left, current_sum+node.val, targetSum)
        right = self.dfs(node.right, current_sum+node.val, targetSum)

        return left or right 