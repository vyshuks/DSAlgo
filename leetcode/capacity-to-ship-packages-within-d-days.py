"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left+right)//2
            
            if self.can_ship(weights, mid, days):
                right = mid
            else:
                left = mid+1
        return left
    
    def can_ship(self, weights, min_weight, days):
        no_days = 1
        w = 0
        
        for weight in weights:
            
            w += weight
            
            if w > min_weight:
                no_days+=1
                w = weight
                
        return no_days <= days
        
        
        
        