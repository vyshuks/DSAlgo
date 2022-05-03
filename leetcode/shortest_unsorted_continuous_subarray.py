"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        
        if len(nums) < 2:
            return 0
        
        low = 0
        while low < end and nums[low] <= nums[low+1]:
            low+=1
        
        
        high = end
        while nums[high] >= nums[high-1] and high-1 >= 0:
            high-=1
            
        if low == end:
            return 0
        
        _min = min(nums[low:high+1])
        _max = max(nums[low:high+1])
        
        
        while low-1 >= 0 and _min < nums[low-1]:
            low-=1
        
        
        while high+1<=end and _max > nums[high+1]:
            high+=1
            
        
        return (high-low)+1
            
        
        
        