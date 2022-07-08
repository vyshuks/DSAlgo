"""
https://leetcode.com/problems/paint-house-iii/
"""

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        memo = {}
        def helper(i, l, t):
            if t > target:
                return float('inf')
            if i == m:
                if t == target:
                    return 0
                else:
                    return float('inf')
            if (i,l,t) in memo:
                return memo[(i,l,t)]
            
            ans = float('inf')
            
            if houses[i] == 0:
                for j in range(n):
                    ans = min(ans, cost[i][j]+helper(i+1, j+1, t if l==j+1 else t+1))

            else:
                ans = min(ans, helper(i+1,houses[i], t if l==houses[i] else t+1))
                
            memo[(i,l,t)] = ans
            return ans
                    
        
        
        
        ans = helper(0, 0, 0)
        return -1 if ans == float('inf') else ans
                    
                    
                        
                    
                    
            
            
        