"""
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
"""
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        l = len(s)
        if l%2 != 0:
            return False
        
        bal = 0
        
        for i in range(len(s)):
            if s[i]=='(' or locked[i]=='0':
                bal+=1
            else:
                bal-=1
            
            
        
        
            if bal< 0:
                return False
        
        bal = 0
        
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or locked[i]=='0':
                bal+=1
            else:
                bal-=1
            
            
            if bal <0:
                return False
        return True
        
            
        