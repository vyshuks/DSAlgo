"""
https://leetcode.com/problems/jump-game-iv/
"""

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = set()
        vertex = {}
        n = len(arr)
        
        if n <= 1:
            return 0
        
        
        
        for i, a in enumerate(arr):
            if a in vertex:
                vertex[a].append(i)
            else:
                vertex[a] = [i]
        q = [0]
        visited.add(0)
        ans = 0
        
        while q:
            nex = []
            for index in q:
                if index == n-1:
                    return ans
                
                for elm in vertex[arr[index]]:
                    if elm not in visited:
                        visited.add(elm)
                        # q.append(elm)
                        nex.append(elm)
                vertex[arr[index]].clear()
                        
                
                for elm in [index-1,index+1]:
                    if elm >= 0 and elm < n and elm not in visited:
                        visited.add(elm)
                        # q.append(elm)
                        nex.append(elm)
            ans+=1
            q = nex
            
        return -1
                    
        