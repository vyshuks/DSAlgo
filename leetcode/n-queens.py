"""
https://leetcode.com/problems/n-queens/
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        def dfs(lst, excluded_pos):
            r = len(lst)
            if r < n:
                for c in range(n):
                    if (r,c) in excluded_pos:
                        continue
                    tmp = "."*(c)+'Q'+"."*(n-c-1)
                    ex = set()
                    
                    for r1 in range(n):
                        ex.add((r1, c))
                    
                    c2 = c
                    r2 = r
                    while c2 < n:
                        r2+=1
                        c2+=1
                        ex.add((r2,c2))
                        
                    c3=c
                    r3=r
                    while c3>0:
                        c3-=1
                        r3+=1
                        ex.add((r3,c3))
                    
                    dfs(lst+[tmp], excluded_pos|ex)
                        
                    
            else:
                output.append(lst)
                
        dfs([], set())
        
        return output
        