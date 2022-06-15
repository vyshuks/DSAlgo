"""
https://leetcode.com/problems/longest-string-chain/
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        memo = {}
        
        def find_longest_chain(word):
            if word not in words_set:
                return 0
            if word in memo:
                return memo[word]
            N = len(word)
            mx = 0
            for i in range(N):
                w = word[:i]+word[i+1:]
                mx = max(mx, find_longest_chain(w)+1)
            memo[word] = mx
            return mx
        
        for word in words:
            find_longest_chain(word)
            
        return max(memo.values())