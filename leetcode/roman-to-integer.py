"""
https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        N = len(s)
        output = 0
        for i in range(N-1, -1, -1):
            if i < N-1 and lookup[s[i]] < lookup[s[i+1]]:
                output-=lookup[s[i]]
            else:
                output += lookup[s[i]]
        return output
            
        