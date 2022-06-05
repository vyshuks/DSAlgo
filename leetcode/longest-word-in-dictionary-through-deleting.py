"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
    
        def helper(sub, whole):
            S,W = len(sub), len(whole)
            i=j=0
            
            while i<S and j<W:
                if sub[i] == whole[j]:
                    i+=1
                j+=1
            
            return i==S
        
        for w in dictionary:
            if helper(w, s):
                return w
        return ""
            
        