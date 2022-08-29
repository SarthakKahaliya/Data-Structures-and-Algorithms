class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array = [None for i in range(len(nums) + 1)]
        
        for val in nums:
            array[val] = val
            
        
        for i in range(len(array)):
            if array[i] == None:
                return i