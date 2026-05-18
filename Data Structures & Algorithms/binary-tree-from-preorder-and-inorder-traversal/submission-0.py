# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # KEY: 
        # Take first element of preorder → that's the root.
        # Find that root in inorder → everything before it is left subtree's nodes, everything after is right subtree's nodes.
        # Recursively build left subtree and right subtree.
    
    # KEY CODE TECHNIQUES: 
        # Preorder is the root-revealer: "root-left-right" 
        # Inorder is the structure-revealer: "left-root-right" 

        # So that the core thing here is to understand how to slice the array
        # left_inorder   = inorder[:mid]     
        # right_inorder  = inorder[mid+1:]   
        # left_preorder  = preorder[1:1+mid]  
        # right_preorder = preorder[1+mid:]  

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: 
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        left_inorder = inorder[:mid] # Key: eliminate the [mid] element
        right_inorder = inorder[mid+1:]
        left_preorder = preorder[1:1+mid] # Key: eliminate the [0] element here 
        right_preorder = preorder[1+mid:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
