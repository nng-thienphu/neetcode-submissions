# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists: 
            return None
        
        # run until the final list come
        while len(lists) > 1: 
            merged = [] # contains all new merged lists here

            # pair 2 list at the same time -> step = 2
            for i in range(0, len(lists), 2): 
                l1 = lists[i] 
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            
            # replace old list with new list 
            lists = merged 
        
        return lists[0]

    

    def mergeTwoLists(self, l1: List[ListNode], l2: List[ListNode]): 
        dummy_start = ListNode(0)
        tail = dummy_start 

        p1 = l1
        p2 = l2

        while p1 and p2: 
            if p1.val < p2.val: 
                tail.next = p1 
                p1 = p1.next
            else: 
                tail.next = p2
                p2 = p2.next

            tail = tail.next
        
        # attach whatever left, one of them is None: 
        tail.next = p1 if p1 else p2


        return dummy_start.next


        

