"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        res = 0
        for num in nums:
            s = k-num
            
            if s in d and d[num] > 0 and d[s] > 0:
                if num == s and d[num] == 1:
                    continue
                res+=1
                d[num]-=1
                d[s]-=1
            
            
        return res