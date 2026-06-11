# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()           # always a real node — no None checks
            result.append(node.val)
            if node.right:               # push RIGHT first...
                stack.append(node.right)
            if node.left:                # ...so LEFT pops first → preorder order
                stack.append(node.left)
        return result