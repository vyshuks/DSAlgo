"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
import heapq
from typing import List


def kth_largest_element_in_array(nums: List[int], k: int) -> int:
    my_heap = [-num for num in nums]
    heapq.heapify(my_heap)

    for _ in range(k-1):
        heapq.heappop(my_heap)
    return -heapq.heappop(my_heap)


print(kth_largest_element_in_array([1,2,3,4,5], 3))
