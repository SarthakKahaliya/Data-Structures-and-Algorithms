class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0;
        
        value = 0
        
        while value <= n:
            value = 4**i
            
            if value == n:
                return True
            elif value > n:
                return False
            
            i += 1