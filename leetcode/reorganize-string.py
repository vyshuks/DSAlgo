"""
https://leetcode.com/problems/reorganize-string/
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        
        c = Counter(s)
        
        heap = [ (-value, key) for key, value in c.items() ]
        
        heapq.heapify(heap)
        
        res = []
        
        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            
            res.append(char1)
            res.append(char2)
            
            
            
            if count1 + 1:
                heapq.heappush(heap, (count1+1, char1))
            
            if count2+1:
                heapq.heappush(heap, (count2+1, char2))
                
        
        if heap:
            count1, char1 = heapq.heappop(heap)
            
            if count1 != -1 or (res and char1 == res[-1]):
                return ""
            else:
                res.append(char1)
                
        return "".join(res)
            
            
            
        