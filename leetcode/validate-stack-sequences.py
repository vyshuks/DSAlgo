"""
https://leetcode.com/problems/validate-stack-sequences/
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        L = len(pushed)
        i = 0
        
        for p in pushed:
            stack.append(p)
            while stack and i< L and stack[-1] == popped[i]:
                stack.pop()
                i+=1
            
        
        return stack == []
        