class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ans = set()
        last = len(nums)
        for i, val in enumerate(nums):
            val = abs(val)
            if val == last:
                last = None
            if val != len(nums): 
                if nums[val] > 0:
                    nums[val] = -nums[val]
                    
            
        for i in range(len(nums)):
            if i != 0:
                if nums[i] > 0:
                    ans.add(i)
                    
        if last:
            ans.add(last)
            
        return ans
                    
        
            