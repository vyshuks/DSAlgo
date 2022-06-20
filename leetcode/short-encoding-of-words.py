"""
https://leetcode.com/problems/short-encoding-of-words/
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end = []
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        self.end.append((node, len(word)+1))
            

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        t = Trie()
        
        for word in words:
            t.insert(word[::-1])
        
        return sum([depth for node, depth in t.end if len(node.children)==0])
            
        