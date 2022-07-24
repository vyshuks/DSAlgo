"""
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
"""

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        ans = pos = neg = 0
        
        for num in nums:
            if num > 0:
                pos+=1
                neg = neg + 1 if neg else 0
            elif num < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
                
            else:
                neg = pos = 0
                
            
            ans = max(ans, pos)
            
        return ans
        # [1,-2,-3,4]
        # pos : 1, 0, 3, 4
        # neg : 0, 2, 1
        # ans: 1, 1, 2