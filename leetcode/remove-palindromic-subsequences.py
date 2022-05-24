"""
https://leetcode.com/problems/remove-palindromic-subsequences/
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        return 2 if s!=s[::-1] else 1