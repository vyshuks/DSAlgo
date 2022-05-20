"""
https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:
    def __init__(self):
        self.output = 0
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R,C = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0]*C for _ in range(R)]
        
        for i in range(0,C):
            if obstacleGrid[0][i] == 1: break
            dp[0][i]=1
            
        for i in range(0,R):
            if obstacleGrid[i][0] == 1: break
            dp[i][0]=1
            
        
        for i in range(1,R):
            for j in range(1,C):
               
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
        return dp[-1][-1]
                    
        