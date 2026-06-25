class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        curr_count = 0
        global_count = 999999999

        for right in range(k-1, len(blocks)): 
            curr_count = 0 
            left = right - k + 1 

            while left <= right: 
                print(left)
                if blocks[left] == "W": 
                    curr_count += 1
                left += 1 
            
            global_count = min(global_count, curr_count)


        return global_count 