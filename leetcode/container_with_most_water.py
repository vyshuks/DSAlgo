"""
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List

def max_area(heights: List[int]) -> int:
    _max_area = 0
    left = 0
    right = len(heights)-1

    while left < right:
        _max_area = max(_max_area, min(heights[left], heights[right]) * (right-left))
        if heights[left] < heights[right]:
            left+=1
        else:
            right-=1
    return _max_area


print(max_area([1,8,6,2,5,4,8,3,7]))

