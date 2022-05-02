"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)-1
        
        col = 0
        
        while row >= 0 and col <= len(matrix[0])-1:
            print(row,col)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                col+=1
            
            else:
                row-=1
        return False
        