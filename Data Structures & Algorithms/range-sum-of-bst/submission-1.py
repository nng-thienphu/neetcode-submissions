# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0 

        stack = [] 

        curr = root

        while curr or stack: 
            if curr: 
                if low <= curr.val and curr.val <= high: 
                    total += curr.val

                if curr.right: 
                    stack.append(curr.right) 
                curr = curr.left
            else: 
                curr = stack.pop()
        
        return total  