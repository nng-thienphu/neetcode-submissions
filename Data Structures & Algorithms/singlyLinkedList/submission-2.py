class ListNode: 
    def __init__(self, val = 0, nextNode = None): 
        self.val = val 
        self.next = nextNode

class LinkedList:
    def __init__(self):
        dummy = ListNode(-1)
        self.head = self.tail = dummy
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0 

        while i < index and curr: 
            curr = curr.next
            i += 1 
        if curr: 
            return curr.val
        return -1 

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val) 
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next: 
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val) 
        self.tail.next = newNode 
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head 
        i = 0

        while i < index and curr : 
            curr = curr.next
            i += 1 
        
        if curr and curr.next: 
            if curr.next == self.tail: 
                self.tail = curr 
            curr.next = curr.next.next 
            return True
        
        return False 

    def getValues(self) -> List[int]:
        curr = self.head.next 
        res = [] 

        while curr: 
            res.append(curr.val) 
            curr = curr.next
        
        return res

        
