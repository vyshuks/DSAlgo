"""
https://leetcode.com/problems/jump-game/
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        last_position = l - 1

        for i in range(l-1, -1 ,-1):
            # print(i)
            
            if (i + nums[i]) >= last_position:
                last_position = i
        return last_position == 0