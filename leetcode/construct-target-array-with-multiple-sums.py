"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-num for num in target]
        heapq.heapify(heap)
        total = sum(target)
        
        while heap[0]!=-1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1: return False
            num %= total
            total += num
            heappush(heap, -num or -total)
            
        return True