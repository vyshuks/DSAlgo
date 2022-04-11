"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""

import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldier(row: List[int])-> int:
            start = 0
            end = len(row) - 1
            while start <= end:
                mid = start + (end-start)//2
                if row[mid] == 1:
                    start = mid+1
                elif row[mid] == 0:
                    end = mid-1
            return start
        
        
        data = []
        for i, row in enumerate(mat):
            data.append((-1*count_soldier(row), -i))
        
        heapq.heapify(data)
        for d in data:
            if len(data) > k:
                heapq.heappop(data)
            
        result = []
        while data:
            result.append(-1*data[0][1])
            heapq.heappop(data)
            
        return result[::-1][:k]
        
        