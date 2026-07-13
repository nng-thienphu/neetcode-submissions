class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks) 
        if total % 4 != 0: 
            return False
        target = total // 4

        # Optimization: Sort matchsticks in descending order to fail faster
        matchsticks.sort(reverse=True)
        

        side = [0,0,0,0] 

        def backtrack(i): 
            if i == len(matchsticks): 
                return True

            for bucket in range(4): 
                if side[bucket] + matchsticks[i] <= target: 
                    side[bucket] += matchsticks[i] 
                    if backtrack(i+1): 
                        return True 
                    side[bucket] -= matchsticks[i] 
                
                if side[bucket] == 0: 
                    break
            
            return False

        return backtrack(0)