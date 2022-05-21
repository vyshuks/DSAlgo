"""
https://leetcode.com/problems/coin-change/
"""

def coinChange(coins: List[int], amount: int) -> int:
        
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0 # base condition
        
        for amt in range(amount+1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1+dp[amt-coin])
                
                
        return dp[amount] if dp[amount] < amount+1 else -1