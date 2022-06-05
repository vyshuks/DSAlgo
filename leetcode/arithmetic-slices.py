"""
https://leetcode.com/problems/arithmetic-slices/
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total =0
        curr=0
        N=len(nums)
        for i in range(2,N):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                curr+=1
                total+=curr
            else:
                curr=0
        return total
        