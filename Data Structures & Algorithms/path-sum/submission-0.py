# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # METHOD: Breadth first search
    # KEY 1: Queue stores (node, running_sum) pairs
    #.    this is general problem of BFS 
    #     if we want to solve this problem we need to add a way to accumulate the sum
    #.    using: queue = [(node, sum_so_far), ...]
    #     so when you pop a node, you also get the cummulative sum upn and including that node
    #     push a child to queue -> push (child, sum_so_far + child.val)

    # KEY 2: Only check running_sum == targetSum 
    #.          when node.left is None and node.right is None
    #.    The problem says "root-to-leaf path." So you can't just check the sum at any node — you have to check it only
    #.     when the node is a leaf (no left AND no right child).
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # edge case:
        if not root: 
            return False
        
        queue = deque() # = [(node1, sum1), (node2, sum2), ... ]
        queue.append([root, root.val]) 

        while queue: 
            for _ in range(len(queue)) : 
                node, total = queue.popleft()

                # Base case: 
                # Leaf check: a leaf has no children on EITHER side.
                if not node.left and not node.right:
                    if total == targetSum:
                        return True


                if node.left: 
                    queue.append([node.left, total + node.left.val]) 
                if node.right: 
                    queue.append([node.right, total + node.right.val])
                
        return False
