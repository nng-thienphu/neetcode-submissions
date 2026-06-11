class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best = None
        def inorder(node):
            nonlocal best
            if not node:
                return
            inorder(node.left)                                   # left
            if best is None or abs(node.val - target) < abs(best - target):
                best = node.val                                  # visit — strict < keeps smaller on ties
            inorder(node.right)                                  # right
        inorder(root)
        return best