class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output= [] 

        # i: index at nums[i]
        # remaining: how much left to reach 
        # path: list of what we have built so far at the leaf node
        def dfs(i, remaining, path): 
            # successful base case
            if remaining == 0: 
                output.append(path.copy())
                return
            # failed base case 
            if remaining < 0 or i == len(nums): 
                return 

            # KEY: 
            #   Upper bound: how many copies of num[i] fit in remaining
            #   Lower bound: start as 0, can skip this element 
            for copies in range(0, (remaining // nums[i]) + 1): 
                path.extend([nums[i]] * copies) 
                # move to the next element in original nums list
                dfs(i+1, remaining - copies * nums[i], path)

                # backtracking step, remove one by one
                for _ in range(copies): 
                    path.pop()
                
        dfs(0, target, []) 
        return output
                
            
        

         