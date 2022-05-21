"""
https://leetcode.com/problems/distribute-candies/
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_types = len(set(candyType))
        l = len(candyType)
        max_candy = l//2
        
        return min(max_candy, candy_types)