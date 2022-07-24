"""
https://leetcode.com/problems/clone-graph/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        cloned = {}
        
        cloned[node] = Node(node.val, [])
        
        q = deque([node])
        
        while q:
            cur = q.popleft()
            
            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                    
                cloned[cur].neighbors.append(cloned[neighbor])
        
        return cloned[node]
                
                    
        