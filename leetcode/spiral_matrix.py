"""
https://leetcode.com/problems/spiral-matrix/
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        if r == 1 or r == 0:
            return matrix[0]
        c = len(matrix[0])
        
        top, right, bottom, left = 0, c-1, r-1, 0
        
        result = []
        def cond():
            return  (left <= right and top <= bottom)
  
        
             
        while cond():
            
            for i in range(left, right+1):
                result.append(matrix[top][i])
            
            top+=1
            
            
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            
            right-=1
            
            if cond():
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])

                bottom-=1
            
            if cond():
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])

                left+=1
        return result
                
        