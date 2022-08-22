class Solution:
    def isPowerOfFour(self, n: int) -> bool:
 #       i = 0;
        
#         value = 0
        
#         while value <= n:
#             value = 4**i
            
#             if value == n:
#                 return True
#             elif value > n:
#                 return False
            
#             i += 1

        if n <= 0:
            return False
        result = math.log(n, 4)
        print(result)
        result = int(result)
        
        print(result)
        if 4**result == n:
            return True
        else:
            return False