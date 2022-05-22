"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def helper(l,r):
            while l>=0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        res = ""
        for i in range(n):
            test = helper(i,i)
            if len(res) < len(test):
                res=test
            test = helper(i,i+1)
            if len(res) < len(test):
                res=test
        return res