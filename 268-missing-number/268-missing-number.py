class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         array = [None for i in range(len(nums) + 1)]
        
#         for val in nums:
#             array[val] = val
            
        
#         for i in range(len(array)):
#             if array[i] == None:
#                 return i
        
        # highest no. is 
        lastNum = len(nums)
        
        for i, num in enumerate(nums):
            lastNum ^= i ^ num
            
        return lastNum
        