class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        if x != self.parent[x]: 
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        if self.find(x) == self.find(y): 
            return True
        
        return False

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x) 
        root_y = self.find(y) 

        if root_x != root_y: 
            if self.size[root_x] < self.size[root_y]: 
                self.size[root_y] += self.size[root_x]
                self.parent[root_x] = root_y
            else: 
                self.size[root_x] += self.size[root_y]
                self.parent[root_y] = root_x
            self.num_components -= 1
            return True
        else: 
            return False

    def getNumComponents(self) -> int:
        return self.num_components