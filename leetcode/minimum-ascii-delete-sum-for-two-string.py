"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        L1,L2 = len(s1),len(s2)
        
        dp = [[0]* (L1+1) for _ in range(L2+1)]
        
        for i in range(1, L1+1):
            dp[0][i] = dp[0][i-1] + ord(s1[i-1])
        
        for i in range(1, L2+1):
            dp[i][0] = dp[i-1][0] + ord(s2[i-1])
            
        for i in range(1, L2+1):
            for j in range(1, L1+1):
                if s1[j-1]==s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(ord(s2[i-1])+dp[i-1][j], ord(s1[j-1])+dp[i][j-1])
        return dp[-1][-1]
        