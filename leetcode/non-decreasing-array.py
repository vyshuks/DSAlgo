"""
https://leetcode.com/problems/non-decreasing-array/
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        L = len(nums)
        mx = float('-inf')
        mn = float('inf')
        n = 0
        m = 0
        for i in range(L):
            if nums[i] < mx:
                n+=1
            mx = max(mx, nums[i])
        
        for i in range(L-1,-1,-1):
            if nums[i]>mn:
                m+=1
            mn = min(mn, nums[i])
            
                
        return n <=1 or m<=1
        