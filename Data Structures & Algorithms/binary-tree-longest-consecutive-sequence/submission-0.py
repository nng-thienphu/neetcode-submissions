# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = 0  # global maximum
        count = 1 # current state

    
        def dfs(node, count): 
            nonlocal best 
            if not node: 
                return

            if count > best: 
                best = count 

            if node.right: 
                if node.right.val - node.val == 1: 
                    dfs(node.right, count + 1)
                else: 
                    dfs(node.right, count) 
                # print(f"node right value: {node.right.val}")
            

            if node.left: 
                if node.left.val - node.val == 1: 
                    dfs(node.left, count + 1)
                else: 
                    dfs(node.left, count)


        dfs(root, count)

        return best