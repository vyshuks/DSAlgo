"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0
        L = len(words)
        
        d = defaultdict(set)
        
        for word in words:
            for c in word:
                d[word].add(c)
        
        ans = 0
        
        
        for i in range(L):
            for j in range(i+1, L):
                if not (d[words[i]] & d[words[j]]):
                    ans = max(ans, len(words[i])*len(words[j]))                    
        return ans
            
        
        