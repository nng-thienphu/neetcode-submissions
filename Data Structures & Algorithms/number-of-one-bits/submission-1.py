class Solution:
    # KEY: Remmeber the trick of applying & 1
    # everything accept for the last bit will be 0 
    # -> so count = last bit 
    def hammingWeight(self, n: int) -> int:
        count = 0 
        while (n!=0) : 
            count += n & 1
            n >>= 1 
        
        return count 