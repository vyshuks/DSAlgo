"""
https://leetcode.com/problems/car-pooling/
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        cur_passenger = 0
        heap = []
        
        for trip in trips:
            num_passenger, start, end = trip
            
            
            while heap and start >= heap[0][0]:
                cur_passenger -= heap[0][1]
                heapq.heappop(heap)
            
            
            cur_passenger+=num_passenger
            
            if cur_passenger > capacity:
                return False
            
            heapq.heappush(heap, [end, num_passenger])
            
        return True
        