class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If descending order, don't need to sell
        # Brute Force method:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
