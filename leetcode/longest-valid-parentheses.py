"""
https://leetcode.com/problems/longest-valid-parentheses/
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        for i,n in enumerate(s):
            if n == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i-stack[-1])
        return mx
                    
    
        