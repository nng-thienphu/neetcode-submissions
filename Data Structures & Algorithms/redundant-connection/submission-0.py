class Solution:
    def __init__(self): 
        self.par = {}
        self.rank = {}

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(1, len(edges) + 2): 
            self.par[i] = i
            self.rank[i] = 0
            
        for edge in edges: 
            mark = self.union(edge) 
            if mark == False: 
                return edge
        

    def union(self, edge_list: List[int]): 
        p1, p2 = self.find(edge_list[0]), self.find(edge_list[1]) 

        if p1 == p2: 
            return False 
        
        if self.rank[p1] > self.rank[p2]: 
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]: 
            self.par[p1] = p2
        else: 
            self.par[p1] = p2
            self.rank[p2] += 1

        return True  
        

    def find(self, n): 
        p = self.par[n] 

        # KEY: 
        # Climb up the parent pointers until we reach the root, i.e. "is p its own parent?"
        # The trick is that
        # when we set up the union tree, we assigned the parent of a root to be itself.
        # This is only true for the root.    
        while p != self.par[p]: 
            self.par[p] = self.par[self.par[p]] 
            p = self.par[p] 
        
        return p
