"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        arr = ["a"] * n
                

        required = k-n
        i = n-1
        while required > 0:
            m = min(25, required)
            arr[i] = chr(ord('a')+m)
            required-=m
            i-=1
        return "".join(arr)
