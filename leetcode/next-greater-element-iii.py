"""
https://leetcode.com/problems/next-greater-element-iii/
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        digits = list(str(n))
        L = len(digits)
        for i in range(L-1, -1, -1):
            if digits[i] > digits[i-1]:
                break
                
        f = i-1
        
        if f==-1:
            return -1
        
        for i in range(L-1, -1, -1):
            if digits[f] < digits[i]:
                break
        
        s = i
        
        digits[f], digits[s] = digits[s], digits[f]
        # print(digits[f+1:][::-1])
        
        res = digits[0:f+1] + digits[f+1:][::-1]
        # print(res)
        res = int("".join(res))
        if res >= 2**31 or res==n:
            return -1
        return res
        
        