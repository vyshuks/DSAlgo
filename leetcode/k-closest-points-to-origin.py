"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = x**2 + y**2

            if len(heap) >= K:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
            if len(heap) < K:
                heapq.heappush(heap, (-dist, x, y))

        return [[x,y] for _,x,y in heap]
        