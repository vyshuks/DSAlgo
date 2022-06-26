"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        N = len(cardPoints)
        left, right = 0 , N-k
        total = sum(cardPoints[right:])
        res = total
        while right < N:
            
            total += (cardPoints[left] - cardPoints[right])
            res = max(res, total)
            left+=1
            right+=1
            
        return res
    
        
       
        