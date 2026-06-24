# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = 0 

        def dfs(node): 
            nonlocal max_avg

            if node is None: 
                return (0, 0)

            left = dfs(node.left) 
            right = dfs(node.right) 

            count = (left[1]+right[1] + 1) 
            total = (left[0] + right[0] + node.val) 

            max_avg = max(max_avg, total / count)

            return (total, count)

        dfs(root)
        return max_avg 
