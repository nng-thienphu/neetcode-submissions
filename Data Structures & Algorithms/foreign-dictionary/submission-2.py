class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create an adj list indegree (smaller) -> node -> adj list (bigger)
        # create indegree array
        n = len(words)
        adj = {}
        indegree = {}
        adj = {c: [] for w in words for c in w}
        indegree = {c: 0 for w in words for c in w} 

        for i in range(1, n): 
            w1 = words[i-1] 
            w2 = words[i] 

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            
            for j in range(len(w1)): 
                if j >= len(w2): 
                    break 
                
                # if w1[j] not in adj: 
                #     adj[w1[j]] = []
                # if w1[j] not in indegree: 
                #     indegree[w1[j]] = 0 
                # if w2[j] not in indegree: 
                #     indegree[w2[j]] = 0  
                # if w2[j] not in adj: 
                #     adj[w2[j]] = [] 

                if w1[j] != w2[j]: 
                    adj[w1[j]].append(w2[j]) 
                    indegree[w2[j]] += 1 
                    break

        print(adj) 
        print(indegree)

        # loop through indegree array and minus 1 
        q = deque()
        for key,value in indegree.items(): 
            if value == 0: 
                q.append(key) 
        
        result = []
        while q: 
            node = q.popleft()
            result.append(node)
            for neighbor in adj[node]: 
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: 
                    q.append(neighbor)
        
        # prune 3: if there is a cycle
        if len(result) < len(indegree): 
            return ""
            
        return "".join(result)
    
        