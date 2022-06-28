"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        seen = set()
        res = 0
        
        for k,v in c.items():
            while v and v in seen:
                res+=1
                v-=1
            seen.add(v)
        return res
            
        