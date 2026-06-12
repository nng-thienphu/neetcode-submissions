class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        hashset = set()
        self.result = False 

        def postorder(node, add_set_flag): 
            if not node or self.result: 
                return
            
            postorder(node.left,add_set_flag)
            postorder(node.right, add_set_flag)

            if add_set_flag: 
                hashset.add(node.val)
            else: 
                remain = target - node.val 
                if remain in hashset:
                    self.result = True

        postorder(root2, True)
        postorder(root1, False) 

        return self.result