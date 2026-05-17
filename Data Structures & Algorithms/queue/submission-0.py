class Node: 
    def __init__(self, val = 0, prev = None, next = None): 
        self.val = val
        self.prev = prev
        self.next = next 

class Deque:
    def __init__(self):
        self.head = Node()
        self.tail = Node() 

        self.head.next = self.tail
        self.tail.prev = self.head 
        self.size = 0 

    def isEmpty(self) -> bool:
        if self.size == 0: 
            return True 
        else: 
            return False 

    def append(self, value: int) -> None:
        newNode = Node(value) 
        prevNode = self.tail.prev

        # link new node
        newNode.prev = prevNode
        newNode.next = self.tail

        # link neighbor
        self.tail.prev = newNode
        prevNode.next = newNode

        self.size += 1

    def appendleft(self, value: int) -> None:
        # assign node
        nextNode = self.head.next 
        newNode = Node(value) 

        # link new node
        newNode.prev = self.head 
        newNode.next = nextNode 
        
        # link neighboor 
        self.head.next = newNode 
        nextNode.prev = newNode

        self.size += 1 

    def pop(self) -> int:
        if self.size == 0: 
            return -1
        
        nodeRemove = self.tail.prev 
        tempVal = nodeRemove.val

        nodeRemove.prev.next = self.tail
        self.tail.prev = nodeRemove.prev

        self.size -= 1 
        return tempVal

    def popleft(self) -> int:
        if self.size == 0: 
            return -1 
        
        nodeRemove = self.head.next
        tempVal = nodeRemove.val

        self.head.next = nodeRemove.next
        nodeRemove.next.prev = self.head

        self.size -= 1 

        return tempVal

