"""
https://leetcode.com/problems/maximum-product-subarray/
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        curMax, curMin = nums[0], nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            tmp = curMax*num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(tmp, curMin*num, num)
            res = max(res, curMax, curMin)
            
        return res
        