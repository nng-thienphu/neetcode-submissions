# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #### handle if k > size of the chain, then it will have the repeated cycle#### 
        # then the new k become the k %n
        if not head or not head.next: 
            return head 
        size = 0 
        node = head
        while node: 
            node = node.next
            size += 1
        if k >= size: 
            k = k%size
        if k == 0:  # equal to the size mean nothing change 
            return head

        #### 2 pointers code #### 
        dummy = ListNode(0, head) 
        left = right = dummy

        for _ in range(k):  
            # delete the left.next node => range(k + 1)
            # deelte the left node => range(k)
            right = right.next
        
        while right.next: 
            right = right.next
            left = left.next
        
        temp = dummy.next
        dummy.next = left.next
        left.next = None
        right.next = temp
    
        return dummy.next



