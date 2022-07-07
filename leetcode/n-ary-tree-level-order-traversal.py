"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        
        res = []
        
        while q:
            
            q_len = len(q)
            level = []
            for _ in range(q_len):
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            res += [level]
                
        return res
                
        