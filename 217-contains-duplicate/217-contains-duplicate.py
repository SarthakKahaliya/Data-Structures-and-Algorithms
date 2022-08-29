class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        
        for val in nums:
            if val in hashMap:
                return True
            else:
                hashMap[val] = True
                
        return False

#         nums.sort()
    
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
            
#         return False