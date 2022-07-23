"""
https://leetcode.com/problems/koko-eating-bananas/
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left+right)//2
            
            if self.can_eat(piles, mid, h):
                right = mid
            else:
                left = mid+1
                
        return left
    
    def can_eat(self, piles, speed, h):
        hours = 0
        for pile in piles:
            if speed >= pile:
                hours+=1
            else:
                hours += math.ceil(pile/speed)
                
        return hours <= h
        