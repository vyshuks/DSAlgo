"""
https://leetcode.com/problems/sum-of-distances-in-tree/
"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.root_sum = 0
        graph = defaultdict(list)
        
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
            
        
        visited = set()
        count = [1]*n
        output = [0]*n
        
        def dfs(cur, parent, depth):
            
            c = 1
            for child in graph[cur]:
                if child != parent:
                    self.root_sum+= (depth+1)
                    c+=dfs(child, cur, depth+1)
            count[cur] = c
            return c
        
        def dfs2(cur, parent, ans):
            output[cur] = ans
            for child in graph[cur]:
                if child!=parent:
                    dfs2(child, cur, ans + (n-count[child])-count[child])
                    
                    
                
            
            
            
        dfs(0,-1,0)
        dfs2(0,-1,self.root_sum)
        return output
            
        