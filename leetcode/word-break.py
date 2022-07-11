"""
https://leetcode.com/problems/word-break/
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        W = set(wordDict)
        
        memo = {}
        def helper(i):
            
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(i, len(s)):
                string = s[i:j+1]
                if string in W:
                    if helper(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
            
        return helper(0)