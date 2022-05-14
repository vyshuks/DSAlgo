"""
https://leetcode.com/problems/word-ladder-ii/
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(set)
        wordset = set(wordList + [beginWord])
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for word in wordList+[beginWord]:
            for i in range(len(word)):
                w1, w2 = word[0:i], word[i+1:]
                for a in alpha:
                    tmp = w1 + a + w2
                    
                    if tmp in wordset and tmp != word:
                        graph[word].add(tmp)
                
            
        
        q = deque([[beginWord]])
        visited = set()
        step = 0
        res = []
        
        while q:
            cur_layer = set()
            for _ in range(len(q)):
                
                word = q.popleft()

                if word[-1] == endWord:
                    res.append(word)



                for w in graph[word[-1]]:
                    if w not in visited:
                        q.append(word+[w])
                        cur_layer.add(w)
                
            visited.update(cur_layer)
            
        
        return res
        