"""
https://leetcode.com/problems/prefix-and-suffix-search/
"""

class WordFilter:

    def __init__(self, words: List[str]):
        self.p = defaultdict(set)
        self.s = defaultdict(set)
        seen = set()
        L = len(words)
        for i in range(L-1,-1,-1):
            word = words[i]
            if word in seen:
                continue
            seen.add(word)
            L = len(word)
            for k in range(L+1):
                self.p[word[:k]].add(i)
                self.s[word[k:]].add(i)
            
        

    def f(self, prefix: str, suffix: str) -> int:
        prefix_set = self.p[prefix]
        suffix_set = self.s[suffix]
        res = suffix_set &  prefix_set
        return max(res) if res else -1