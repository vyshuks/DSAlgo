"""
https://leetcode.com/problems/stone-game-ii/
"""

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        total = sum(piles)
        P = len(piles)
        self.memo = {}
        
        # @lru_cache(None)
        def helper(p,M,i):
            if i >= P:
                return 0
            if (i,M) in self.memo:
                return self.memo[(i,M)]
            
            tot = 0
            ans = float('-inf')
            for j in range(2*M):
                
                if i+j < P:
                    tot+=p[i+j]
                M1=max(M, j+1)
                ans = max(ans, tot-helper(p,M1, i+j+1))
                
            self.memo[(i,M)]=ans
            return ans
        
        diff = helper(piles, 1, 0)
        return (total+diff)//2
                    
                
        