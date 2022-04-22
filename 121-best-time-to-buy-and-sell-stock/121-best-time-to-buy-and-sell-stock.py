class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j += 1
            elif prices[i] <= prices[j]:
                maxP = max(maxP, prices[j] - prices[i])
                j += 1
        
        return maxP