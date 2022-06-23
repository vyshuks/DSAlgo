"""
https://leetcode.com/problems/next-greater-element-ii/
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        N = len(nums)
        
        res = [-1]*N
        
        for i in range(2*N-1, -1, -1):
            while stack and stack[-1] <= nums[i%N]:
                stack.pop()
                
            res[i%N] = stack[-1] if stack else -1
            stack.append(nums[i%N])
            
        return res
                
            
        