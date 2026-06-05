# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [] 
        curr = root

        RESULT = [] 

        while curr or stack: 
            if curr : 
                # print(curr.val) 
                RESULT.append(curr.val)

                # KEY: keep the right subset in the waitlist
                if curr.right: 
                    stack.append(curr.right) 
                # Then keep going to the leaf node of left subset
                curr = curr.left
            else: 
                # go to the recent right as stack LIFO
                curr = stack.pop()
        
        return RESULT