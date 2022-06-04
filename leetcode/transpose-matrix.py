"""
https://leetcode.com/problems/transpose-matrix/
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R,C = len(matrix), len(matrix[0])
        
        ans = [[0]*R for _ in range(C)]
        
        for i in range(R):
            for j in range(C):
                ans[j][i] = matrix[i][j]
        
        return ans
        