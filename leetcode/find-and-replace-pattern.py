"""
https://leetcode.com/problems/find-and-replace-pattern/
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for word in words:
            d = {}
            d1={}
            found = True
            for p,w in zip(pattern, word):
                if p in d and d[p] !=w:
                    found=False
                    break
                
                if w in d1 and d1[w] != p:
                    found = False
                    break
                
                d[p] = w
                d1[w]=p
            if found:
                res.append(word)
                
        return res
                
            
                
        