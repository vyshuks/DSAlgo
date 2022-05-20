"""
https://leetcode.com/problems/unique-paths-iii/
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        
        start_r,start_c,end_r,end_c=0,0,0,0
        empty = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    start_r,start_c=i,j
                elif grid[i][j]==2:
                    end_r,end_c=i,j
                elif grid[i][j]==0:
                    empty+=1
        
        self.output=0
        visited=set()
        
        def dfs(r,c,visited,walk):
            if r==end_r and c==end_c:
                    if walk==empty+1:
                        self.output+=1
                    return
            if 0<=r<R and 0<=c<C and grid[r][c]!=-1 and (r,c) not in visited:
                visited.add((r,c))
                for r1,c1 in [(0,-1),(0,1),(1,0),(-1,0)]:
                    new_row = r+r1
                    new_col = c+c1
                    
                    dfs(new_row,new_col,visited,walk+1)
                visited.remove((r,c))
        dfs(start_r,start_c,visited,0)
                
        
        
        return self.output
        