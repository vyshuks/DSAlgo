"""
https://leetcode.com/problems/missing-number/
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_tot = ((n)*(n+1))//2
        current_tot = sum(nums)
        
        return actual_tot-current_tot
        
