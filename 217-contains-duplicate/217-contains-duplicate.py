class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        
        for val in nums:
            if val in hashMap:
                return True
            else:
                hashMap[val] = True
                
        return False