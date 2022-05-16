"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot, l = sum(nums), len(nums)
        
        if tot%2 != 0:
            return False
        
        target = tot//2
        memo = {}
        def rec(level,nums, target):
            if (level,target) in memo:
                return memo[(level,target)]
            if target == 0:
                return True
            if level == l:
                return False
            
            memo[(level,target)] = rec(level+1, nums, target-nums[level]) or rec(level+1, nums, target)
            return memo[(level,target)]
        return rec(0, nums, target)
        