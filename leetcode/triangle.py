"""
https://leetcode.com/problems/triangle/
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        L = len(triangle)
        if L==1:
            return triangle[0][0]
        
        dp = triangle[-1]
        
        for index in range(L-2, -1,-1):
            for i,num in enumerate(triangle[index]):
                dp[i] = num + min(dp[i], dp[i+1])
        
        return dp[0]
                
        