class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0

        curr_count = 0
        global_count = 999999999

        for right in range(len(blocks)): 
            if blocks[right] == "W": 
                curr_count += 1 
            
            if right - left + 1 == k: 
                global_count = min(global_count, curr_count)
                if blocks[left] == "W": 
                    curr_count -= 1
                left += 1 
        
        return global_count