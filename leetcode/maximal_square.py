"""
https://leetcode.com/problems/maximal-square/
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_height = 0
        _row = len(matrix)
        if _row == 0:
            return 0
        _col = len(matrix[0])

        _s = [[0] * (_col+1) for _ in range(_row+1)]

        for i in range(1, _row+1):
            for j in range(1, _col+1):
                if matrix[i-1][j-1] == "1":
                    _s[i][j] = min(_s[i-1][j], _s[i][j-1], _s[i-1][j-1]) + 1
                    max_height = max(max_height, _s[i][j])
        return max_height * max_height
        