"""
https://leetcode.com/problems/queens-that-can-attack-the-king/
"""

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        seen = [[False]*8 for _ in range(8)]
        
        def is_inside(r,c):
            return 0<=r<8 and 0<=c<8
        
        for q in queens:
            r,c = q
            seen[r][c]=True
        
        dirs = [(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,-1),(-1,1)]
        
        
        result = []
        
        for d1,d2 in dirs:
            x1, y1 = king
            while is_inside(x1+d1,y1+d2):
                x1+=d1
                y1+=d2
                
                if seen[x1][y1]:
                    result.append([x1,y1])
                    break
                
                
        return result
            
            
        