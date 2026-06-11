class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(root): 
            nonlocal best
            if not root: 
                return 0
            
            left = dfs(root.left) 
            right = dfs(root.right)
            best = max(best, left + right) # keep global max

            return 1 + max(left, right)
        dfs(root) 
        return best