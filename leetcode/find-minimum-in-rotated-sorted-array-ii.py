"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0; r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[r] < nums[mid]:
                # min is b/w mid and r
                l = mid + 1
            elif nums[r] > nums[mid]:
                # min lies to the left as in an unrotated array
                r = mid
            else:
                # we dont know  where the min lies, so we shorten the  search window 
                r -= 1
        return nums[l]
        