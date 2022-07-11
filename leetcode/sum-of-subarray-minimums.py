"""
https://leetcode.com/problems/sum-of-subarray-minimums/
"""

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        n = len(A)
        
        q = deque()
        left = [1]*n
        
        q.append((A[0], 1))
        
        for i in range(1, n):
            while q and q[-1][0] >= A[i]:
                _ , inc = q.pop()
                left[i]+= inc
            q.append((A[i], left[i]))
            
        right = [1]*n
        q = deque()
        q.append((A[-1], 1))
        
        for i in range(n-2, -1, -1):
            while q and q[-1][0] > A[i]:
                _, inc = q.pop()
                right[i]+=inc
                
            q.append((A[i], right[i]))
            
            
        ans = 0
        
        
        for i in range(n):
            ans += left[i]*A[i]*right[i]
            
        return ans % (10**9+7)
        