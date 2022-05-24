"""
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dist_sub = 2**k
        l = len(s)
        tracker = set([s[i:i+k] for i in range(l+1-k)])
        return dist_sub == len(tracker)
        