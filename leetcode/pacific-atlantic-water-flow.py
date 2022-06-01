"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        R = len(heights)
        C = len(heights[0])
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        pacific = []
        atlantic = []
        
        pacific_set = set()
        atlantic_set = set()
        
        for i in range(C):
            pacific.append((0,i))
            atlantic.append((R-1, i))
        
        for i in range(R):
            pacific.append((i,0))
            atlantic.append((i, C-1))
            
        def dfs(r,c,visited):
            visited.add((r,c))
            
            for d1,d2 in dirs:
                new_r, new_c = d1+r, d2+c
                
                if 0 <= new_r < R and 0<= new_c < C and heights[r][c] <= heights[new_r][new_c] and (new_r,new_c) not in visited:
                    dfs(new_r,new_c,visited)
        for r,c in pacific:
            dfs(r,c, pacific_set)
        
        for r,c in atlantic:
            dfs(r,c, atlantic_set)
            
        return pacific_set & atlantic_set
        
        
        
                    
                    
        