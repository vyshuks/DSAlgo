"""
https://leetcode.com/problems/design-underground-system/
"""

class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.path = {}
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        data = self.checkins[id]
        del self.checkins[id]
        key = (data[0], stationName)
        d = abs(data[1]-t)
        new_d = self.path.get(key, [0, 0])[0] + d
        new_count = self.path.get(key, [0, 0])[1] + 1

        self.path[key] = [new_d, new_count ]
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data = self.path.get((startStation, endStation), [0,0])
        return data[0]/data[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)