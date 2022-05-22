"""
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
"""

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        n = len(capacity)
        res = 0
        c = [0]*n
        for i in range(n):
            c[i] = capacity[i]-rocks[i]
        
        c.sort()
        
        for i in range(n):
            if additionalRocks >= c[i]:
                additionalRocks-=c[i]
                res+=1
        return res
        