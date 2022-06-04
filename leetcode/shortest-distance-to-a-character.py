"""
https://leetcode.com/problems/shortest-distance-to-a-character/
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        L = len(s)
        left, right = [None]*L, [None]*L
        
        tmp = float('inf')
        
        for i in range(L):
            if s[i] == c:
                tmp=0
            left[i] = tmp
            tmp+=1
            
        tmp = float('inf')
        for i in range(L-1, -1, -1):
            if s[i]==c:
                tmp=0
            right[i] = tmp
            tmp+=1
        
        output = []
        for i in range(L):
            t = min(left[i],right[i])
            output.append(t)
            
        return output
        