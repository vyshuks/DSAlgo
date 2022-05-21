"""
https://leetcode.com/problems/set-mismatch/
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        tot = n*(n+1)//2
        tot_without_repeat = sum(set(nums))
        tot_with_repeat = sum(nums)
        
        return [tot_with_repeat-tot_without_repeat, tot-tot_without_repeat]
        