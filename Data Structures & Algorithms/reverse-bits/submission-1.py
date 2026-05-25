class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
        index = 0 

        while index < 32: 
            if n&1 == 1 : 
                result += 2**(31-index)
            index +=1 
            n >>= 1 
        
        return result