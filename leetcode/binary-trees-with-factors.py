"""
https://leetcode.com/problems/binary-trees-with-factors/
"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        d = defaultdict(int)
        arr.sort()
        N=len(arr)
        for i in arr:
            temp=1
            for j in arr:
                if j > i:
                    break
                temp+= d[j]*d[i/j]
            d[i] = temp
        return sum(d.values())%(10**9+7)
                    
        