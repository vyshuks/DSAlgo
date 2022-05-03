"""
https://leetcode.com/problems/broken-calculator/
"""

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans+=1
            if target%2 == 0:
                target = target//2
            else:
                target+=1
        return ans + (startValue-target)
        