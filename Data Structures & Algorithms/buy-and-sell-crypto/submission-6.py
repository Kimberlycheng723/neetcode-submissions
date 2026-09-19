class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for sell in prices:
            profit = sell - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, sell)
        return maxProfit


