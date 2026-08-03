# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        left = right = dummy 

        for _ in range(n+1): # one node of standing room for the surgeon
            # we want to delete left.next, not deleting left node 
            right = right.next
        
        while right: 
            right = right.next
            left = left.next

        left.next = left.next.next 

        return dummy.next 