class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuyPrice = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - lowestBuyPrice)
            lowestBuyPrice = min(lowestBuyPrice, price)
        return maxProfit

