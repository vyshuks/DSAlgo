"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        
        start = 0
        output = 0
        for num in num_set:
            if num-1 not in num_set:
                start = num
                while start in num_set:
                    start+=1
                output = max(output, start-num)
                
        return output