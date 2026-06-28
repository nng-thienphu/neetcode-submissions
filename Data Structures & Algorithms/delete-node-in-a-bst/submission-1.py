# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self, root) -> Optional[TreeNode]: 
        curr = root
        while curr and curr.left: 
            curr = curr.left 
        return curr 

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # if nothing found = key, return null
            return None 
        
        # loop to find the node need to be delete 
        #    if key > node: move right 
        #    if key < node: move left  
        if key > root.val: # 
            root.right = self.deleteNode(root.right, key) 
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key) 
        else: # if key = current node 
            ## base case for recursive 
            if not root.left: 
                return root.right
            elif not root.right: 
                return root.left
            
            ## recursive -> go right subtree -> remove the repeated node 
            else: 
                ### go to the right subtree from the key -> then find the left most value
                minNode = self.minValueNode(root.right)  

                ### exchange the key value to the left most value
                root.val = minNode.val 
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root 

        
