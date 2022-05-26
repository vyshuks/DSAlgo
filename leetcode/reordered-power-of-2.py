"""
https://leetcode.com/problems/reordered-power-of-2/
"""

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        c = Counter([int(i) for i in str(n)])
        
        i=0
        n=0
        
        while n<=10**9:
            n = 2**i
            d = Counter([int(j) for j in str(n)])
            if d==c:
                return True
            i+=1
        return False
        