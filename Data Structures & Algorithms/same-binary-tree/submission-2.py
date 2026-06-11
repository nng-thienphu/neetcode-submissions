class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        waitlist_q = [] 
        wailitst_p = []

        result = [] 
        
        while q or p or waitlist_q or wailitst_p : 
            if p and q: 
                if p.val != q.val: 
                    return False

                wailitst_p.append(p.right)
                waitlist_q.append(q.right)
                p = p.left
                q = q.left
            elif p or q:
                return False
            else: 
                p = wailitst_p.pop()
                q = waitlist_q.pop()

        return True