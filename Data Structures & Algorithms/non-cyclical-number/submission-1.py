class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.helperSquareSum(n)  
        
        while slow != fast:     
            fast = self.helperSquareSum(fast) 
            fast = self.helperSquareSum(fast) 
            slow = self.helperSquareSum(slow)
        
        return True if slow == 1 else False 

    def helperSquareSum(self, n): 
        count = 0 
        
        while n: 
            digit = n % 10
            count += digit ** 2

            n = n//10
        
        return count 
