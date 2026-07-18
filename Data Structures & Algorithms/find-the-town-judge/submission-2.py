class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # step 1. convert into adj 
        adj = {} 
        trusted_by = {}

        for i in range(1, n+1): 
            adj[i] = []
        
        for s, d in trust: 
            adj[s].append(d) 
            trusted_by[d] = trusted_by.get(d, 0) + 1 


        for key, value in adj.items(): 
            if not value and trusted_by[d] == n-1  : 
                return key
        
        return -1

