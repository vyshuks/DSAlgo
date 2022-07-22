"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if k == 0:
            return [target.val]
        
        graph = defaultdict(list)
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
                
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
                
        visited = set([target])
        q = deque()
        q.append((target, 0))
        
        res = []
        
        while q:
            node, distance = q.popleft()
            
            if distance == k:
                res.append(node.val)
            else:
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        q.append((child, distance+1))
                        
        return res
                
        