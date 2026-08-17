# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if not root: 
            return []
        
        hashmap = {}
        q = deque([(root, 0)])  # node, col 

        while q: 
            node,c = q.popleft() 
            if c not in hashmap: 
                hashmap[c] = [] 
            hashmap[c].append(node.val) 

            if node.left: 
                q.append([node.left, c-1]) 
            if node.right: 
                q.append([node.right, c+1]) 
        
        return [hashmap[c] for c in sorted(hashmap)]
