"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack:
                obj = stack[-1]
                
                if obj[0] == char:
                    stack[-1] = [obj[0], obj[1]+1]
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([char, 1])
                    
            else:
                stack.append([char, 1])
        
        
        return "".join([s[0]*s[1] for s in stack])
        