class UnionFind: 
    def __init__(self, n): 
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n
    
    def find(self, x): 
        if x != self.parent[x]: 
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y): 
        x_parent = self.find(x)
        y_parent = self.find(y) 

        if x_parent != y_parent: 
            if self.size[x_parent] < self.size[y_parent]: 
                self.parent[x_parent] = y_parent
                self.size[y_parent] += self.size[x_parent] 
            else: 
                self.parent[y_parent] = x_parent
                self.size[x_parent] += self.size[y_parent]
            
            self.num_components -= 1 
            return True
        return False 
         

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        ROWS = len(isConnected) 
        COLS = len(isConnected[0])
        n = ROWS
        unionClass = UnionFind(n)

        for r in range(ROWS): 
            for c in range(COLS): 
                if isConnected[r][c] == 1: 
                    unionClass.union(r,c) 
        
        return unionClass.num_components 
