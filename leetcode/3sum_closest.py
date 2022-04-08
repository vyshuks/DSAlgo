"""
https://leetcode.com/problems/3sum-closest/
"""
from typing import List

def three_sum_closest(nums: List[int], target)->int:
    l = len(nums)
    target_sum = float('inf')
    nums.sort()
    for i in range(l-2):
        left = i+1
        right = l-1
        while left < right:
            s = nums[left] + nums[right] + nums[i]
            if abs(target-s) < abs(target-target_sum):
                target_sum = s
            if target < s:
                right-=1
            else:
                left+=1
            
    return target_sum


print(three_sum_closest([-1,2,1,-4], 1))
