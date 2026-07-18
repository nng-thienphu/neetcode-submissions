class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # step 1. convert into adj 
        incoming = {} 
        outgoing = {} 

        for i in range(1, n+1): 
            incoming[i] = 0 
            outgoing[i] = 0 
        
        for s, d in trust: 
            incoming[d] += 1 
            outgoing[s] += 1 


        for i in range(1, n+1): 
            if incoming[i] == n-1 and outgoing[i] == 0: 
                return i

        return -1 
