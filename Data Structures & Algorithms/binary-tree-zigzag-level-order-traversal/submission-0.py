# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return [] 
            
        q = deque([root])    
        res = [] 
        step = -1 

        while q: 
            size = len(q) 
            step *= -1 
            level = [] 
            for _ in range(size): 
                curr = q.popleft()
                level.append(curr.val)

                if curr.left: 
                    q.append(curr.left) 
                if curr.right : 
                    q.append(curr.right)
            
            res.append(level[::step]) 
        
        return res
