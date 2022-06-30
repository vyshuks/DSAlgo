"""
https://leetcode.com/problems/jump-game-v/
"""

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        def dp(arr, index, memo):
            if memo is None:
                memo = {}
            if index in memo:
                return memo[index]
            ans = 1
            j = index+1
            
            while j <= min(n-1, index+d) and arr[j]<arr[index]:
                ans = max(ans, 1 + dp(arr,j,memo))
                j+=1
            
            j=index-1
            while j >= max(0, index-d) and arr[j]<arr[index]:
                ans = max(ans, 1 + dp(arr,j,memo))
                j-=1
            memo[index] = ans
            return ans
        
        ans = 1
        memo = {}
        for i in range(n):
            ans = max(ans, dp(arr,i,memo))
        return ans
            
            
                
            
            