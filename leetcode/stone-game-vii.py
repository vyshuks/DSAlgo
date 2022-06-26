"""
https://leetcode.com/problems/stone-game-vii/
"""

class Solution:
    
    def stoneGameVII(self, stones: List[int]) -> int:
        
        
        
        self.dp = [[-1] * len(stones) for _ in range(len(stones))]
        def helper(left, right, total):
            if left >= right:
                return 0
            if self.dp[left][right] != -1:
                return self.dp[left][right]
            # if (left, right) in self.memo:
            #     return self.memo[(left,right)]
            
            left_ans = total - stones[left] - helper(left+1, right, (total - stones[left]))
            right_ans = total - stones[right] - helper(left, right-1, total - stones[right])
            
            ans = max(left_ans, right_ans)
            # self.memo[(left,right)] = ans
            self.dp[left][right] = ans
            return ans
        
        return helper(0, len(stones)-1, sum(stones))
        