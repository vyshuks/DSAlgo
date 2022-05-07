"""
https://leetcode.com/problems/132-pattern/
"""
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = len(nums)
        
        stack = []
        last = float('-inf')
        
        for i in range(l-1,-1,-1):
            if nums[i]<last:
                return True
            while stack and stack[-1]<nums[i]:
                last=stack.pop()
            stack.append(nums[i])
        return False
        