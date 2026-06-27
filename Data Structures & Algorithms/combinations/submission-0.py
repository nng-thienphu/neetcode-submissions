class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(e, currentSet, result, n, k): 
            # e: number (from 1 to n) 
            # currentSet = current built so far on this branch
            # result = shared result list
            # n, k = upper bound and target size

            # step 1. base case (1) reach target number amount (2) pass avaiable number n
            if len(currentSet) == k: # reach k numbers
                result.append(currentSet.copy()) 
                return  # stop, no more number to add
            
            if e > n: 
                return
            
            # step 2. decide to include i
            currentSet.append(e)
            helper(e+1, currentSet, result, n, k) 

            # step 3. decide to skip i 
            currentSet.pop()
            helper(e+1, currentSet, result, n,k)

        result = []
        helper(1, [], result, n, k) 
        return result