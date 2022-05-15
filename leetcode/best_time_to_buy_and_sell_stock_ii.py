"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = len(prices)
        for i in range(l-1):
            if prices[i+1] > prices[i]:
                profit += (prices[i+1] - prices[i])

        return profit
        