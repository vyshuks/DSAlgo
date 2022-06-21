"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ans = 0
        
        l = 0
        r = len(nums)-1
        m =0
        
        while l < r:
            m = (l+r)//2
            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r=m
                
        return nums[l]
                
        