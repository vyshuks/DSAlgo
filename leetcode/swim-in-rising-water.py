"""
https://leetcode.com/problems/swim-in-rising-water/
"""

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (grid[0][0], 0, 0))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        visited = set()
        
        output = 0
        
        while heap:
            max_height, row, col = heapq.heappop(heap)
            output = max(output, max_height)
            
            if (row,col) == (rows-1, cols-1):
                break
                
            for rx, cx in directions:
                rx+=row
                cx+=col
                if 0<=rx<rows and 0<=cx<cols and (rx,cx) not in visited:
                    heapq.heappush(heap, (grid[rx][cx], rx, cx))
                    visited.add((rx,cx))
                
            
        return output
        
        
        