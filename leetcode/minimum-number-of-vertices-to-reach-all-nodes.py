"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parent = [False]*n
        
        for u,v in edges:
            parent[v]=True
        
        ans = []
        for u in range(n):
            if not parent[u]:
                ans.append(u)
        return ans
            
        