"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
"""

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        memo = {}
        def dp(d ,target):
            if d==0:
                return target == 0
            if (d, target) in memo:
                return memo[(d,target)]
            
            tot = 0
            for num in range(1, f+1):
                tot+=dp(d-1,target-num)
            memo[(d,target)] = tot
            return tot
        
        return dp(d,target) % (10**9 + 7)
    
                
            
            
        