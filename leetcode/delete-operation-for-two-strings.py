"""
https://leetcode.com/problems/delete-operation-for-two-strings/
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1 , L2= len(word1), len(word2)
        dp = [[0]*(L1+1) for _ in range(L2+1)]
        
        for c in range(L1+1):
            dp[0][c] = c
        
        for r in range(L2+1):
            dp[r][0] = r
            
        
        for i in range(1,L2+1):
            for j in range(1,L1+1):
                if word1[j-1]==word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]