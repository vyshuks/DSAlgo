"""
https://leetcode.com/problems/last-stone-weight/
"""
from typing import List
import heapq


def last_stone_weight(stones: List[int]) -> int:
    l = len(stones)
    if l == 0:
        return 0
    if l == 1:
        return stones[0]
        
    my_heap = [-stone for stone in stones]
    heapq.heapify(my_heap)
    while True:
        stone1 = -1 * heapq.heappop(my_heap)
        stone2 = -1 * heapq.heappop(my_heap)
        if stone1 == stone2:
            if len(my_heap) == 0:
                return 0
        else:
            new_stone = abs(stone1-stone2)
            heapq.heappush(my_heap, -new_stone)
        if len(my_heap) == 1:
            return -1 * heapq.heappop(my_heap)