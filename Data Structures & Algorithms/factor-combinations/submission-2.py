class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def backtrack(remaining, start, path):
            # Option (a): remaining declares itself the final factor
            #   - path non-empty  → blocks the trivial [n]
            #   - remaining >= start → keeps the list non-decreasing (no duplicates)
            if path : 
                res.append(path + [remaining])

            # Option (b): peel off a small factor i and recurse
            for i in range(start, int(remaining ** 0.5) + 1):
                if remaining % i == 0:
                    backtrack(remaining // i, i, path + [i])

        backtrack(n, 2, [])
        return res