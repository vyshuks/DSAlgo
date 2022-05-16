"""
https://leetcode.com/problems/wildcard-matching/
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        R = len(s)
        C = len(p)

        dp = [[False]*(C+1) for _ in range(R+1)]


        dp[0][0] = True # both string and pattern is empty

        for i in range(1, C+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-1]

        for i in range(1, R+1):
            for j in range(1, C+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[(i-1)][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[(i-1)][j]
                else:
                    dp[i][j] = False
                    

        
        return dp[R][C]

    





print(isMatch("abcd", "abc*d"))