# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # step 1. heap for K ListNode
        heap = [] 
        for index, node in enumerate(lists): 
            if node: 
                heapq.heappush(heap, (node.val, index, node)) 

        # step 2. heap pop and connect the min to the current linked list 
        curr = ListNode(0) 
        dummyNode = curr 
        
        while heap: 
            val, index, node = heapq.heappop(heap)
            curr.next = node

            # move the linked list 
            curr = curr.next 
            
            # step 3. add its successor 
            node = node.next
            if node: 
                heapq.heappush(heap, (node.val, index, node)) 
        
        return dummyNode.next 

        