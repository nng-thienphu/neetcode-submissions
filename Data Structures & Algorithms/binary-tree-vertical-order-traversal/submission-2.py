# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = {}

        def dfs(row, col, node): 
            if not node: 
                return
            if col not in hashmap: 
                hashmap[col] = [] 
            hashmap[col].append([row, node.val]) 
            dfs(row+1, col-1, node.left) 
            dfs(row+1, col+1, node.right)
        
        dfs(0,0, root) 
        
        result = [] 
        for key in sorted(hashmap): 
            sorted_node = sorted(hashmap[key], key = lambda x: x[0]) 
            result.append([val for row, val in sorted_node])
        
        return result