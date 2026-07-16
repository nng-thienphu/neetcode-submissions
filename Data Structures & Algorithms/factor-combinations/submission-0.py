class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def backtrack(remaining, start, path):
            # remaining can be the final factor if:
            # - path is non-empty (blocks [n] itself)
            # - remaining >= start (keeps non-decreasing order)
            if path and remaining >= start:
                res.append(path + [remaining])

            i = start
            while i * i <= remaining:      # factors only up to sqrt(remaining)
                if remaining % i == 0:
                    backtrack(remaining // i, i, path + [i])
                i += 1

        backtrack(n, 2, [])
        return res