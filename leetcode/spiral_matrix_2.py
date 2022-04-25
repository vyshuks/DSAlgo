"""
https://leetcode.com/problems/spiral-matrix-ii/
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        top, right, bottom, left = 0, n-1, n-1, 0
        num = 1
        matrix = [[1]*n for _ in range(n)]
        while top <= bottom and left <= right:
            
            for i in range(left, right+1):
                matrix[top][i] = num
                num+=1
            top+=1
            
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num+=1
            
            right-=1
            
            
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num+=1
            
            
            bottom-=1
            
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num+=1
            
            left+=1
        
        return matrix
            
                