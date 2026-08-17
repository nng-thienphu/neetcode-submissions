# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heightDict = {} 

        def postorder(node): 
            if not node: 
                return -1
            
            left = postorder(node.left) 
            right = postorder(node.right) 
            height = max(left, right) + 1 

            if height not in heightDict: 
                heightDict[height] = []
            heightDict[height].append(node.val)
        
            return height
        
        postorder(root)
        
        res = [] 
        
        for key, value in sorted(heightDict.items()): 
            res.append(value) 
        
        return res
            
        