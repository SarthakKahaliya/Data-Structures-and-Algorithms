class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        
        output = []
        
        for i, val in enumerate(nums):
            output.append(prefix)
            prefix *= val
            
        print(output)
        
        l = len(nums) - 1
        
        while l > -1:
            output[l] = output[l] * postfix
            postfix *= nums[l]
            l -= 1
            
        return output