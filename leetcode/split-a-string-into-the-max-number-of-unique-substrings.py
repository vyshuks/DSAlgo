"""
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def helper(i , temp):
            if i == len(s):
                return 0
            
            temp+=s[i]
            op1, op2 = 0, 0
            if temp not in seen:
                seen.add(temp)
                op1 = 1+helper(i+1, "")
                seen.remove(temp)
            op2 = helper(i+1, temp)
            
            return max(op1, op2)
        
        return helper(0, "")