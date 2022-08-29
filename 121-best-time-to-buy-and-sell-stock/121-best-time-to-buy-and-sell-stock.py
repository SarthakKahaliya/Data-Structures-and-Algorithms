class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0
        
        profit = 0
        
        lowest = prices[0]
        highest = prices[0]
        
        for val in prices:
            if lowest > val:
                lowest = val
                highest = val
                print(lowest, highest)
                
                
            if highest < val:
                highest = val
                diff = highest - lowest
                profit = max(profit, diff)
                print(profit)
                print(lowest, highest)
                
                
        
        return profit
                
                
        