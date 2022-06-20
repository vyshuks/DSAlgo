"""
https://leetcode.com/problems/count-nodes-with-the-highest-score/
"""

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = defaultdict(list)
        
        for i,v in enumerate(parents):
            graph[v].append(i)
        print(graph)
        c = Counter()
        P = len(parents)
        
        def count_nodes(node):
            p,s=1,0
            for child in graph[node]:
                res = count_nodes(child)
                p*=res
                s+=res
            p*= max(1, P-1-s)
            c[p]+=1
            return s+1
            
                    
                
        count_nodes(0)
        return c[max(c.keys())]
                    
                    
        