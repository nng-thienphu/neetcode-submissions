# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best = root

        def dfs(root): 
            nonlocal best 
            if not root: 
                return
            
            d_new = abs(root.val - target)
            d_best = abs(best.val - target)
            if d_new < d_best or (d_new == d_best and root.val < best.val): 
                best = root
                
            if root.val >= target: 
                dfs(root.left) 
            else: 
                dfs(root.right)

        dfs(root)
        return best.val 
        
        
        

        