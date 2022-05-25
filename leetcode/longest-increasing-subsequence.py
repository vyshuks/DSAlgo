"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        dp = [1]*L
        for i in range(L-1,-1,-1):
            for j in range(i+1, L):
                if nums[j]>nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)