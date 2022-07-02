"""
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        max_h, max_w = 0, 0
        
        for i in range(1, len(horizontalCuts)):
            diff = abs(horizontalCuts[i] - horizontalCuts[i-1])
            max_h = max(max_h, diff)
            
        for i in range(1, len(verticalCuts)):
            diff = abs(verticalCuts[i] - verticalCuts[i-1])
            max_w = max(max_w, diff)
            
        return (max_h*max_w)%(10**9+7)
        
        
        
        