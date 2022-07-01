"""
https://leetcode.com/problems/jump-game-vii/
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0
        
        while q:
            index = q.popleft()
            start = max(index+minJump, farthest+1)
            
            for i in range(start, min(index+maxJump+1, len(s))):
                if s[i] == '0':
                    q.append(i)
                    if i == len(s)-1:
                        return True
            farthest = index+maxJump
        return False