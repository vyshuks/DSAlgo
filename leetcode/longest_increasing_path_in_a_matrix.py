"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C = len(matrix), len(matrix[0])
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        memo = {}
        
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            output = 1
            for d1,d2 in dirs:
                new_r, new_c = r+d1, c+d2
                if 0 <= new_r <R and 0<= new_c <C and matrix[r][c]<matrix[new_r][new_c]:
                    output = max(output, dfs(new_r, new_c)+1)
            memo[r,c] = output
            return output
        
        output = 0
        for i in range(R):
            for j in range(C):
                output = max(output, dfs(i,j))
                
        return output
                
    
    
        