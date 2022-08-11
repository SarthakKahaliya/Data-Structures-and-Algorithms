class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key is the number and value is the index in the hash map
        hashMap = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            
            if diff in hashMap:
                return [hashMap[diff], index] 
            else:
                hashMap[value] = index 