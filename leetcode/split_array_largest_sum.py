"""
https://leetcode.com/problems/split-array-largest-sum/
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start = max(nums)
        end = sum(nums)
        ans = None
        
        while start <= end:
            mid = start + (end-start)//2
            
            if self.min_subarray_required(nums, mid) <= m:
                end = mid-1
                ans = mid
            else:
                start = mid+1
        return ans
    
    def min_subarray_required(self, nums, mid):
        subarrays = 1
        
        s = 0
        
        for num in nums:
            
            if s+num <= mid:
                s = s + num
            else:
                s = num
                subarrays+=1
        return subarrays
        