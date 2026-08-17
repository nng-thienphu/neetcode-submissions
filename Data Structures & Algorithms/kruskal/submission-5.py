class UnionFind: 
    def __init__(self, n): 
        self.size = [1] * n 
        self.parent = {} 
        for i in range(n): 
            self.parent[i] = i 
    
    def find(self, n): 
        p = self.parent[n] 
        
        while p != self.parent[p]: 
            self.parent[p] = self.parent[self.parent[p]] 
            p = self.parent[p] 
        
        return self.parent[p] 
    
    def union(self, x, y): 
        root_x = self.find(x)
        root_y = self.find(y) 

        if root_x != root_y: 
            if self.size[root_x] <= self.size[root_y]: 
                self.parent[root_x] = root_y 
                self.size[root_y] += self.size[root_x] 
            else: 
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            
            return True 

        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        minWeight = 0 
        edgeCount = 0 

        unionFind = UnionFind(n) 

        for src, dst, w in edges:  
            heapq.heappush(minHeap, [w, src, dst]) 

        while minHeap and edgeCount < n-1: 
            w, src, dst = heapq.heappop(minHeap) 
            if unionFind.union(src, dst): 
                minWeight += w 
                edgeCount += 1 
        
        return minWeight if edgeCount == n-1 else -1 
        