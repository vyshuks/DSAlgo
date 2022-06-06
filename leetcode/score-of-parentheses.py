"""
https://leetcode.com/problems/score-of-parentheses/
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        L = len(s)
        output, mul = 0, 0
        
        for i,c in enumerate(s):
            if s[i] == '(':
                mul+=1
            else:
                mul-=1
                if s[i-1] == '(':
                    output+= 2**mul
        return output