# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def height(node): 
            if node is None:
                return -1
            
            # recursive in height 
            left = height(node.left) 
            right = height(node.right) 
            h = max(left, right) + 1

            # KEY: result is always packed [height 0, height 1, height 2, ...]
            # THIS CODE = am I the FIRST node to reach this height ? 
            if h == len(result): 
                result.append([])
            
            result[h].append(node.val) 

            return h
        height(root) 
        return result 