"""
https://leetcode.com/problems/possible-bipartition/
"""
from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        groups = {i: None for i in range(1,N+1)}
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(v1, grp):
            if groups[v1] is None:
                groups[v1] = grp
            else:
                return groups[v1] == grp

            for n in graph[v1]:
                if not dfs(n, 2 if grp==1 else 1):
                    return False
            return True

        for i in range(1,N+1):
            if not groups[i]  and not dfs(i,1):
                return False

        return True
        