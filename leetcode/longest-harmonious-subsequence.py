"""
https://leetcode.com/problems/longest-harmonious-subsequence/
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        output = 0
        c = Counter(nums)
        
        for k,v in c.items():
            if k+1 in c:
                output = max(output, c[k+1]+c[k])
        return output