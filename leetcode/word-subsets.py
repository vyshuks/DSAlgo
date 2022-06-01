"""
https://leetcode.com/problems/word-subsets/
"""
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        total_words= {}
        
        for word in words2:
            tmp = Counter(word)
            for k,v in tmp.items():
                if k in total_words:
                    total_words[k] = max(total_words[k], v)
                else:
                    total_words[k] = v
                    
        output = []
        for word in words1:
            tmp = Counter(word)
            flag=1
            for k,v in total_words.items():
                if k not in tmp or total_words[k] > tmp[k]:
                    flag=0
            if flag==1:
                output.append(word)
        return output
                    
                
            
        