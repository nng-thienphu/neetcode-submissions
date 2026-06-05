class Solution:
    # KEY INSIGHTS: the way how to solve this problem is nodiniz-ing this list nums 
    #         The value at each position is reinterpreted as "the index to jump to next." 
    #.         A value of 2 means "go to index 2." so the value 2 is edge pointing to node 2
    #.         Because every value is in [1, n], every jump lands on a valid index, so you never fall off the array. 
    #          That's what makes the array a self-contained functional graph 
    
    # KEY CODE TECHNIQUES 1: 
    # Phase 1 ends when slow == fast somewhere inside the cycle. That meeting spot is not the answer.
    # Phase 2 fixes this: reset one pointer back to the start (index 0), then advance both one step at a time, and the point where they meet again is the cycle entrance — the duplicate.

    # KEY CODE TECHNIQUES 2: 
    # normal move: slow = slow.next
    # this problem: slow = nums[slow]
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 

        while True: 
            slow = nums[slow] 
            fast = nums[ nums[fast] ]

            if slow == fast: 
                break
        
        slow2 = 0
        while True: 
            slow = nums[slow] 
            slow2 = nums[slow2] 

            if slow == slow2:
                return slow

        