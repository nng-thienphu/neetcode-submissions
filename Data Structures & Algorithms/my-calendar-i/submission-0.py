class TreeNode: 
    def __init__(self, start: int, end: int): 
        self.start = start
        self.end = end

        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None 
    
    def _insert(self, node: TreeNode, start: int, end: int) -> bool: 
        # add to the left of the node
        if end <= node.start: 
            # dfs to the left
            # until it reach the leaf node - (base case) 
            if not node.left : 
                node.left = TreeNode(start, end) 
                return True 
            return self._insert(node.left, start, end)

        # add to the right
        elif start >= node.end:  
            # dfs to the right
            # until it reach the leaf node - (base case)
            if not node.right: 
                node.right = TreeNode(start, end)
                return True 
            return self._insert(node.right, start, end)
        
        else: 
            return False
        
    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root: # if no booked time found yet
            self.root = TreeNode(startTime, endTime)       
            return True

        return self._insert(self.root, startTime, endTime) 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)