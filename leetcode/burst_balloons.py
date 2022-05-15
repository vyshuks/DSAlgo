"""
https://leetcode.com/problems/burst-balloons/
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        dp = [ [0]*l for _ in range(l) ]
        
        for L in range(l-1, -1, -1):
            for R in range(L, l):
                for i in range(L, R+1):
                    
                    left = 1 if L <= 0 else nums[L-1]
                    right = 1 if R == l-1 else nums[R+1]
                    
                        
                    left_part = 0 if L > i-1 else dp[L][i-1]
                    right_part = 0 if i+1 > R else dp[i+1][R]
                    
                        
                        
                    current_sum = nums[i] * left * right
                    prev_sum = left_part + right_part
                    dp[L][R] = max(dp[L][R], current_sum+prev_sum)
        
        return dp[0][l-1]