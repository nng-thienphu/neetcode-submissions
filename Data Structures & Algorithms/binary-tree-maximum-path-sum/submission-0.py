# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def dfs(node): 
            if not node: 
                return 0

            left_chain = max(dfs(node.left) , 0)  # compare to 0 to make this chain optional if it is negative 
            right_chain = max(dfs(node.right), 0) 

            peak = left_chain + right_chain + node.val # what if the path ends here - never goes higher
            self.best = max(self.best, peak) 

            return node.val + max(left_chain, right_chain) 
        
        dfs(root)
        return self.best 
            