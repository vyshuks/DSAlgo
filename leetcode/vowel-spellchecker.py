"""
https://leetcode.com/problems/vowel-spellchecker/
"""

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        pure_set = set(wordlist)
        cap_list = {}
        vow_list = {}
           
               
        def helper(word):
            vowel = "aeiou"
            tmp=[]
            for c in word.lower():
                if c in vowel:
                    tmp.append("*")
                else:
                    tmp.append(c)
            return "".join(tmp)
        
        for word in wordlist:
            l = word.lower()
            v = helper(word)
            if v not in vow_list:
                vow_list[v] = word
            if l not in cap_list:
                cap_list[l]=word
        
        output = []
        for q in queries:
            if q in pure_set:
                output.append(q)
            
            
            elif q.lower() in cap_list:
                output.append(cap_list[q.lower()])
            
            
            elif helper(q) in vow_list:
                output.append(vow_list[helper(q)])
            else:
                output.append("")
                
        return output
                    
        
        