"""
https://leetcode.com/problems/find-median-from-data-stream/
"""

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))
        

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (self.high[0] - self.low[0])/2
        else:
            return -self.low[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()