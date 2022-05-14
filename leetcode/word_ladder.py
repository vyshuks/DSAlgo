"""
https://leetcode.com/problems/word-ladder/
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
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
                
            
        
        q = deque([(beginWord, 0)])
        visited = set()
        step = 0
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step+1
            
            if word not  in visited:
                visited.add(word)
                for w in graph[word]:
                    if w not in visited:
                        q.append((w, step+1))
        
        return 0