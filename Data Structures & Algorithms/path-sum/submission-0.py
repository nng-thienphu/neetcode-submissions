# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # METHOD: Breadth-First Search
    #
    # KEY 1: The queue stores (node, running_sum) pairs.
    #   This is the general BFS pattern, extended with an accumulator.
    #   When we pop a node, we also get the cumulative sum from root to that node.
    #   When we push a child, we push (child, running_sum + child.val).
    #
    # KEY 2: Only check running_sum == targetSum when the node is a leaf.
    #   The problem requires a root-to-LEAF path, so a node only qualifies
    #   when it has no left AND no right child.
    #
    # NOTE: Unlike level-order traversal, we don't need the `level_size` trick
    #   here because we don't care about grouping nodes by level — we only
    #   care about reaching leaves.
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Edge case: empty tree has no root-to-leaf path.
        if not root:
            return False

        queue = deque()                      # holds (node, running_sum) pairs
        queue.append((root, root.val))       # start with the root and its value

        while queue:
            node, total = queue.popleft()

            # Leaf check: a leaf has no children on EITHER side.
            if not node.left and not node.right:
                if total == targetSum:
                    return True

            if node.left:
                queue.append((node.left, total + node.left.val))
            if node.right:
                queue.append((node.right, total + node.right.val))

        return False