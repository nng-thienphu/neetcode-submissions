class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, path = [], [] 

        def dfs(i): 
            if i == len(s): 
                if len(path) == 4: 
                    res.append('.'.join(path)) 
                return
            
            for j in range(1,4): 
                if i+j > len(s): 
                    continue 
                if (j > 1) and (s[i] == "0" or int(s[i:i+j]) > 255 ): 
                    continue
                
                path.append(s[i:j+i]) 
                dfs(i+j)
                path.pop()

        dfs(0)
        return res 
                                