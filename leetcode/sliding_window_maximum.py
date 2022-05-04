"""
https://leetcode.com/problems/sliding-window-maximum/
"""

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end  = 0
        
        l = len(nums)
        q = collections.deque()
        
        output = []
        
        while end < l:
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            
            q.append(end)
            
            if start > q[0]:
                q.popleft()
            
            if (end-start)+1 ==k:
                output.append(nums[q[0]])
                start+=1
            
            end+=1
        return output
            
                
            
        