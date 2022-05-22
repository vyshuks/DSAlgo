"""
https://leetcode.com/problems/next-greater-element-i/
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = { v: i for i,v in enumerate(nums1)}
        
        stack = []
        res = [-1]*len(nums1)
        
        for i in range(len(nums2)):
            cur = nums2[i]
            
            while stack and cur > stack[-1]:
                elm = stack.pop()
                index = d[elm]
                res[index] = cur
            
            if cur in d:
                stack.append(cur)
        return res
        