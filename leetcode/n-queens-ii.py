"""
https://leetcode.com/problems/n-queens-ii/
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        
        def dfs(row, excluded):
            r = row
            if r < n:
                for c in range(n):
                    if (r,c) in excluded:
                        continue
                    exc = set()
                    
                    # down
                    for r1 in range(r,n):
                        exc.add((r1,c))
                    
                    # right
                    r2=r
                    c2=c
                    while c2 < n:
                        c2+=1
                        r2+=1
                        exc.add((r2,c2))
                    
                    # left
                    r3=r
                    c3=c
                    while c3 > 0:
                        r3+=1
                        c3-=1
                        exc.add((r3,c3))
                    
                    dfs(r+1, excluded|exc)
                    
                    
            else:
                self.ans+=1
        dfs(0, set())
        
        
        return self.ans
        