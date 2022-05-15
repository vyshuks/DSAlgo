"""
https://leetcode.com/problems/interleaving-string/
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        A = len(s1)
        B = len(s2)
        C = len(s3)
        
        if A+B != C:
            return False
        
        memo = {}
        def rec(i,j,k):
            if i==A and j ==B and k==C:
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            b1,b2 = False,False
            if i < A and s1[i] == s3[k]:
                b1 = rec(i+1,j,k+1)
            
            if j < B and s2[j] == s3[k]:
                b2 = rec(i,j+1,k+1)
            memo[(i,j,k)] = b1 or b2
            return b1 or b2
        
        return rec(0,0,0)