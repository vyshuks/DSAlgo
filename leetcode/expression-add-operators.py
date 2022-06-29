"""
https://leetcode.com/problems/expression-add-operators/
"""

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        output = []
        def dfs(i, sofar, res, prev):
            if i >=n :
                # eq = "".join(sofar)
                if res == target:
                    output.append("".join(sofar))
                    
                return
            
            for j in range(i, n):
                cand = int(num[i:j+1])
                if not sofar:
                    dfs(j+1, sofar+[num[i:j+1]], cand, cand)
                else:
                    dfs(j+1, sofar+["+"]+[num[i:j+1]], res+cand, cand)
                    dfs(j+1, sofar+["-"]+[num[i:j+1]], res-cand, -cand)
                    dfs(j+1, sofar+["*"]+[num[i:j+1]], res-prev+cand*prev, cand*prev)
                if num[i] == '0':
                    break
                
        dfs(0, [], 0, None)
        return output
        