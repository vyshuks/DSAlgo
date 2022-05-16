"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        R,C = len(grid), len(grid[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        q = deque()
        q.append((1, (0,0)))
        visited = set()
        
        while q:
            step, coordinates = q.popleft()
            row, col = coordinates
            if row == R-1 and col ==C-1:
                return step
            
            for direction in directions:
                new_row = row+direction[0]
                new_col = col+direction[1]
                if 0<=new_row<R and 0<=new_col<C and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    q.append((step+1, (new_row, new_col)))
                    visited.add((new_row,new_col))
        return -1