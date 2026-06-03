# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# WRONG ASSUMPTION: 
# I tried two pointers from both ends like an array, but this is a singly linked list, so this is wrong 
# I can only go forward, never back. So the right pointer cannot work in this case 

# KEY 1: INSIGHT
# the formula (n-1-i) is basically just a mirror 
# so we need to find the middle point in the whole array
# then reverse the half later to cook it 

# KEY 2: CODE MIDDLE POINT 
# to find the middle point, use the fast and slow pointer technique
# short = curr.next, fast = curr.next.next 

# KEY 3: Code reverse template: 
# def reverse(head):
    # prev = None
    # curr = head
    # while curr:
    #     nxt = curr.next      # 1. save the road forward
    #     curr.next = prev     # 2. flip the arrow backward
    #     prev = curr          # 3. grow the reversed chain
    #     curr = nxt           # 4. step forward
    # return prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        short = head 
        fast = head
        while fast and fast.next: 
            short = short.next
            fast = fast.next.next
        
        # KEY
        # prev (None) -> curr -> nxt
        # the key to reverse is to make nxt is curr 
        # and make curr is prev 
        prev = None
        curr = short
        while curr: 
            nxt = curr.next
            curr.next = prev

            prev = curr 
            curr = nxt 
        # KEY: prev is now the head of the right linked list 

        best = 0 
        while prev: 
            best = max(best, prev.val + head.val)
            prev = prev.next 
            head = head.next
        
        return best 

