"""
https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
"""

class Solution:
    def numOfWays(self, n: int) -> int:
        c2,c3 = 6, 6
        for i in range(n-1):
            c2, c3 = 3*c2 + 2*c3, 2*c3+2*c2     
        
        mod = 10**9+7
        return (c2+c3)%mod
                
                    
        