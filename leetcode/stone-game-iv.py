"""
https://leetcode.com/problems/stone-game-iv/
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]* (n+1)
        
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                if not dp[i-j*j]:
                    dp[i] = True
                    break
                j+=1
                
        return dp[-1]
#         self.memo = {}
        
#         def helper(remain):
#             if remain == 0:
#                 return False
#             if remain in self.memo:
#                 return self.memo[remain]
#             k = 1
#             while k*k <= remain:
#                 if not helper(remain-k*k):
#                     self.memo[remain] = True
#                     return True
#                 k+=1
#             self.memo[remain]=False
#             return False
        
#         return helper(n)

    
        