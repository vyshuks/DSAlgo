"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = []
        
        def flatten(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.nestedList.append(i)
                else:
                    flatten(i.getList())
        flatten(nestedList)
        self.inc = -1
        self.l = len(self.nestedList)
        
    
        
    
    def next(self) -> int:
        self.inc+=1
        return self.nestedList[self.inc]
        
    
    def hasNext(self) -> bool:
        return self.inc+1 <= self.l-1