"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}
        pairs = 0
        
        for song_len in time:
            mod = song_len % 60
            if mod == 0:
                pairs += d.get(mod, 0)
                
            else:
                pairs += d.get(60 - mod, 0)
            
            d[mod] = d.get(mod, 0) + 1
            
        return pairs
        