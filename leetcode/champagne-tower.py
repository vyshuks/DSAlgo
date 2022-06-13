"""
https://leetcode.com/problems/champagne-tower/
"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [poured]
        
        for _ in range(query_row):
            tmp = [0]*(len(glasses)+1)
            for i in range(len(glasses)):
                remaining = (glasses[i]-1)/2
                if remaining > 0:
                    tmp[i] += remaining
                    tmp[i+1] += remaining
                
            glasses = tmp
            
        return min(1,glasses[query_glass])
            
        
        
        