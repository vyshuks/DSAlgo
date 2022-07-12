"""
https://leetcode.com/problems/matchsticks-to-square/
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        perimeter = sum(matchsticks)
        
        if perimeter % 4 != 0:
            return False
        
        side = perimeter // 4
        
        matchsticks.sort(reverse=True)
        
        def dfs(a,b,c,d,i):
            if i==N:
                if a==b==c==d:
                    return True
                return False
            
            m = matchsticks[i]
            if a+m <= side and dfs(a+m,b,c,d,i+1):
                return True
            
            if b+m <= side and dfs(a,b+m,c,d,i+1):
                return True
            
            if c+m <= side and dfs(a,b,c+m,d,i+1):
                return True
            
            if d+m <= side and dfs(a,b,c,d+m,i+1):
                return True
            
            return False
        
        return dfs(0,0,0,0,0)
            
        
        
        