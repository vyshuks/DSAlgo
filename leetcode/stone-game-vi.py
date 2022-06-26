"""
https://leetcode.com/problems/stone-game-vi/
"""

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        scores = []
        
        for i in range(n):
            scores.append((-1*(aliceValues[i] + bobValues[i]), i))
            
        # scores.sort(reverse=True)
        heapq.heapify(scores)
        alice_score, bob_score = 0, 0
        
        # for index, score in enumerate(scores):
        i = 0
        while scores:
            score , index = heapq.heappop(scores)
            if i%2 == 0:
                alice_score += aliceValues[index]
            else:
                bob_score += bobValues[index]
            i+=1
            
                
        res = 0
        if alice_score > bob_score:
            res=1
        elif alice_score < bob_score:
            res=-1
        
        return res
                
            
        