"""
https://leetcode.com/problems/diagonal-traverse/
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        going_up = True
        
        res = []
        
        r = c = 0
        
        while r < rows and c < cols:
            if going_up:
                while r > 0 and c < cols-1:
                    res.append(mat[r][c])
                    r-=1
                    c+=1
                res.append(mat[r][c])
                if c == cols-1:
                    r+=1
                else:
                    c+=1
                    
                going_up = False
                
            else:
                while r < rows-1 and c > 0:
                    res.append(mat[r][c])
                    r+=1
                    c-=1
                res.append(mat[r][c])
                if r == rows-1:
                    c+=1
                else:
                    r+=1
                
                going_up = True
                    
        return res
            
        