"""
https://leetcode.com/problems/permutations/
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        visited = set()
        
        def backtracking(visited, arr):
            if len(arr) == l:
                res.append(arr)
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    backtracking(visited, arr+[num])
                    visited.remove(num)
        
        backtracking(visited, [])
        return res