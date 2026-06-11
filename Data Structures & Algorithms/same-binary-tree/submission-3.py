class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: both empty → identical here
        if not p and not q:
            return True
        # Case 2: exactly one empty → structures differ
        if not p or not q:
            return False
        # Case 3: both exist but values differ → different
        if p.val != q.val:
            return False
        # Case 4: both exist, values match → recurse on both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
