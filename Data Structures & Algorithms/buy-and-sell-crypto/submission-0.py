class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyday, sellday = 0, 1
        maxP = 0

        while sellday < len(prices):
            if prices[buyday] < prices[sellday]:
                profit = prices[sellday] - prices[buyday]
                maxP = max(profit, maxP)
            else:
                buyday = sellday
            sellday +=1
        
        return maxP