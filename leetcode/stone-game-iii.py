"""
https://leetcode.com/problems/stone-game-iii/
"""

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
#         self.memo = {}
        
#         def helper(s, i):
            
#             if i == n:
#                 return 0
#             if i in self.memo:
#                 return self.memo[i]
            
#             ans = float('-inf')
            
#             ans = max(ans, s[i] - helper(s, i+1))
#             if i+1 < n:
#                 ans = max(ans, s[i] + s[i+1] - helper(s, i+2))
            
#             if i+2 < n:
#                 ans = max(ans, s[i]+s[i+1]+s[i+2]-helper(s, i+3))
            
#             self.memo[i] = ans
                
#             return ans
        
#         ans = helper(stoneValue, 0)
#         if ans > 0:
#             return "Alice"
#         elif ans == 0:
#             return "Tie"
#         else:
#             return "Bob"
        
        s = stoneValue
        # dp = [0]*(n+1)
        i_1, i_2, i_3 = 0, 0, 0
        i = n-1
        while i >= 0:
            ans = float('-inf')
            ans = max(ans, s[i] - i_1)
            if i+1 < n:
                ans = max(ans, s[i] + s[i+1] - i_2)
            
            if i+2 < n:
                ans = max(ans, s[i]+s[i+1]+s[i+2]-i_3)
            i_1, i_2, i_3 = ans, i_1, i_2
            i-=1
            
        ans = i_1
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"