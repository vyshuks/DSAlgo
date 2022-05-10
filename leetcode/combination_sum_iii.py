"""
https://leetcode.com/problems/combination-sum-iii/
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def dfs(build, num, sum_so_far):
            if sum_so_far > n:
                return
            
            if len(build) == k and sum_so_far==n:
                result.append(build)
                return
            
            for i in range(num, 10):
                if sum_so_far > n: break
                dfs(build+[i], i+1, sum_so_far+i)
            
        
        dfs([], 1, 0)
        return result
        
        
        