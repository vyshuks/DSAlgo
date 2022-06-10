"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        lookup = {}
        
        start = 0
        
        for i, c in enumerate(s):
            if c in lookup and lookup[c] >= start:
                start = lookup[c]+1
                
            else:
                maxlen=max(maxlen, i-start+1)
            lookup[c] = i
        return maxlen
            
        