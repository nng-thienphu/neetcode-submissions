class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
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

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = [] 
        for n1, n2, weight in edges: 
            heapq.heappush(minHeap, [weight, n1, n2])

        unionFind = UnionFind(n) 

        mst_weight = 0
        edges_count = 0
        while minHeap and edges_count < n - 1:
            weight, n1, n2 = heapq.heappop(minHeap)
            if unionFind.union(n1, n2):
                mst_weight += weight
                edges_count += 1

        return mst_weight if edges_count == n - 1 else -1