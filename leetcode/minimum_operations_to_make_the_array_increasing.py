"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                change = nums[i-1]-nums[i]
                result+= change+1
                nums[i] = nums[i-1] + 1
        return result