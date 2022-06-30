"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        
        res = 0
        
        for num in nums:
            res+= abs(num - nums[mid])
            
        return res
        