class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        # step 1: register every letter as a node
        # (nodes come from ALL characters; edges only from first-differences)
        adj = {c: [] for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}

        # step 2: build edges from adjacent word pairs
        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]

            # invalid input: longer word before its own prefix
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])   # first difference = one edge
                    indegree[w2[j]] += 1
                    break                      # rest carries no information

        # step 3: Kahn's — seed with indegree-0 letters, drain
        q = deque(c for c in indegree if indegree[c] == 0)

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # step 4: cycle check — starved letters mean contradictory ordering
        if len(result) < len(indegree):
            return ""

        return "".join(result)