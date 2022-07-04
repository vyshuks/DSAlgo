"""
https://leetcode.com/problems/candy/
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        N = len(ratings)
        
        output = [1] * N
        
        for i in range(1, N):
            if ratings[i-1] < ratings[i]:
                output[i] = output[i-1] + 1
                
        for i in range(N-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                output[i] = max(output[i+1]+1, output[i])
                
        return sum(output)
        