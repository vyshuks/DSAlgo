"""
https://leetcode.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)
        dp = [0]*(n+1)

        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1

        i=2
        while i <= n:
            if s[i-1] != '0':
                dp[i] = dp[i-1]


            two_digit = s[i-2:i]
            if two_digit and 10 <= int(two_digit) <= 26:
                dp[i] += dp[i-2]
            i+=1

        return dp[-1]
        