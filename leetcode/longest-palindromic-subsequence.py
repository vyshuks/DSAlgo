"""
https://leetcode.com/problems/longest-palindromic-subsequence/
"""

class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return lcs(text1, text2)
        m = len(text1)
        n = len(text2)
        L = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                
                if text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])