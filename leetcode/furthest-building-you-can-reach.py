"""
https://leetcode.com/problems/furthest-building-you-can-reach/
"""

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        L = len(heights)
        i =0
        # for i in range(0, L-1):
        while i < L-1:
            diff = heights[i+1]-heights[i]
            
            if diff <= 0:
                i+=1
                continue
                
            bricks-=diff
            heapq.heappush(heap, -diff)
            
            if bricks < 0:
                b = -1 * heapq.heappop(heap)
                bricks+=b
                ladders-=1
                
            if ladders < 0:
                break
            i+=1
                
        return i
                
                
        