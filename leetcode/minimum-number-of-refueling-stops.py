"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        output = 0
        
        prev = 0
        
        fuel = startFuel
        
        heap = []
        
        for distance,gas in stations+[[target, 0]]:
            fuel -= distance - prev
            
            while heap and fuel < 0:
                fuel += -heapq.heappop(heap)
                output+=1
                
            if fuel < 0:
                return -1           
            
            
            heapq.heappush(heap, -gas)
            
            prev = distance
        
        return output