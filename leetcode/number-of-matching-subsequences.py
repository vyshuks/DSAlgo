"""
https://leetcode.com/problems/number-of-matching-subsequences/
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        lookup = {}
        for i, c in enumerate(s):
            if c in lookup:
                lookup[c].append(i)
            else:
                lookup[c] = [i]
                
        def find_index(lst, i):
            l , r = 0, len(lst)
            while l < r:
                mid = (l+r)//2
                if lst[mid] > i:
                    r = mid
                
                    
                else:
                    l = mid+1
                    
            return l
                
                
        count = 0
        for word in words:
            latest = -1
            found = True
            for w in word:
                if w not in lookup:
                    found = False
                    break
                i = find_index(lookup[w], latest)
                if i == len(lookup[w]):
                    found = False
                    break
                else:
                    latest = lookup[w][i]
            if found:
                count+=1
                
        return count
                    
                
            
                
        
#         def check_substring(s1, s2):
#             i,j = 0, 0
#             m,n = len(s1), len(s2)
            
#             if m > n:
#                 return False
            
#             while i<m and j < n:
#                 if s1[i] == s2[j]:
#                     i+=1
#                 j+=1
                
#             return i == m
        
#         count  = 0
#         matching = set()
#         non_matching = set()
#         for word in words:
#             if word in non_matching:
#                 continue
#             if word in matching or check_substring(word, s):
#                 matching.add(word)
#                 count+=1
#             else:
#                 non_matching.add(word)
#         return count
            
                
        