class Solution:
    # 1. KEY INSIGHT: Parse string using regex 
        #     \{ (.*?) \}     |     ([a-z]+)
        #  option A               option B
    def expand(self, s: str) -> List[str]:
        slots = [] 
        
        for braced, plain in re.findall(r"\{(.*?)\}|([a-z]+)", s): 
            # findall returns tuples, one per chunk of the string:
            #   [('a,b', ''), ('', 'c'), ('d,e', ''), ('', 'f')]
            if braced: 
                slots.append(sorted(braced.split(",")))
                # 'a,b'.split(',') = ['a','b'];  
            else: 
                slots.append([plain])

        n = len(slots)
        res, path = [], []

        def backtrack(start): 
            if len(path) == n: 
                res.append("".join(path))
                return
            
            level = slots[start]
            for char in level: 
                path.append(char)
                backtrack(start+1)
                path.pop()
            
            return res
        
        backtrack(0)
        return res 



