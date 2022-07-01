"""
https://leetcode.com/problems/jump-game-vi/
"""

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        q = deque()
        q.append(0)
        
        
        
        for i in range(1, n):
            
            while q and q[0] < i-k:
                q.popleft()
                
   
            nums[i] += nums[q[0]]
            
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            q.append(i)
            
        return nums[-1]
        
#         h = [(-nums[0], 0)]
        
#         for i in range(1,n):
#             while h[0][1]<i-k:
#                 heappop(h)
#             max_so_far = h[0][0]
#             heappush(h, ((max_so_far-nums[i]),i))
#             if i == n-1:
#                 return -(max_so_far-nums[i])
                     
                     
            
            
            
        