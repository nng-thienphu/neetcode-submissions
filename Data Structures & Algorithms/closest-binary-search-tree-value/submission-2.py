class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        best_d = abs(target - closest)   # cached distance of the champion

        while root:
            d = abs(target - root.val)   # distance of the node we're standing on

            # new champion if strictly closer, or tie broken by smaller value
            if d < best_d or (d == best_d and root.val < closest):
                closest = root.val
                best_d = d

            # binary-search step: walk toward the target
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest