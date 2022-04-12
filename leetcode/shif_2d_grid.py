"""
https://leetcode.com/problems/shift-2d-grid/
"""

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = [len(g) * [0] for g in grid ]
        tot_row = len(grid)
        tot_col = len(grid[0])
        
        for i, g in enumerate(grid):
            for j, r in enumerate(g):
                id_index = (((i * tot_col)+j) +k )% (tot_row*tot_col)
                row = id_index//tot_col
                col = id_index%tot_col
                arr[row][col] = grid[i][j]
        return arr