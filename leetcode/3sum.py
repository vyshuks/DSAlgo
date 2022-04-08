"""
https://leetcode.com/problems/3sum/submissions/
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = len(nums)
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            
            left = i+1
            right = l-1


            while left < right:
                s= nums[left] + nums[right] + nums[i]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1    
                    right-=1
                    left+=1
                elif s>0:
                    right-=1
                else:
                    left+=1
        return result
    
    
    
        