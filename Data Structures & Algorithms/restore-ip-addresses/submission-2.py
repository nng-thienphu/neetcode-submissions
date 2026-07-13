class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, path = [], []

        def dfs(i):
            rem = len(s) - i            # chars left
            need = 4 - len(path)        # segments left

            # PRUNE: too few or too many chars for remaining segments
            if rem < need or rem > need * 3:
                return

            if i == len(s):             # need == 0 guaranteed valid here
                res.append('.'.join(path))
                return

            for j in range(1, 4):
                if i + j > len(s):
                    break               # break, not continue — longer j only gets worse
                seg = s[i:i+j]
                if j > 1 and (seg[0] == "0" or int(seg) > 255):
                    continue

                path.append(seg)
                dfs(i + j)
                path.pop()

        dfs(0)
        return res