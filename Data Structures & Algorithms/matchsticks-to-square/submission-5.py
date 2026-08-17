class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        bucket = [0] * 4 
        total = sum(matchsticks) 
        if total % 4 != 0: 
            return False 
        target = total // 4
        matchsticks.sort(reverse = True)

        def backtrack(i): 
            if i == len(matchsticks): 
                return True
            
            for pos in range(4): 
                if bucket[pos] + matchsticks[i] <= target: 
                    bucket[pos] += matchsticks[i] 
                    if backtrack(i+1): 
                        return True
                    bucket[pos] -= matchsticks[i] 

                if bucket[pos] == 0: 
                    break
            
            return False
        
        return backtrack(0)