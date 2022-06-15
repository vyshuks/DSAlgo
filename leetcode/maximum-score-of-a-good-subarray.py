"""
https://leetcode.com/problems/maximum-score-of-a-good-subarray/
"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        L = len(nums)
        
        minimum = nums[k]
        left, right = k, k
        res =nums[k]
        
        while left >0 or right < L-1:
            if left==0:
                right+=1
            elif right==L-1:
                left-=1
            elif nums[left-1] < nums[right+1]:
                right+=1
            else:
                left-=1
            
            minimum = min(minimum, nums[left], nums[right])
            res = max(res, minimum*(right-left+1))
        return res