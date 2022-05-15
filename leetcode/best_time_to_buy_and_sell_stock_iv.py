"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        if N == 0:
            return 0
        dp = [0] * N
        for t in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1, N):
                profit = max(profit, prices[i] + pos)
                pos = max(pos, dp[i]-prices[i])
                dp[i] = profit
        return dp[-1]