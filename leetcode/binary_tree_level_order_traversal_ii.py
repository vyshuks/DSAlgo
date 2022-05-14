"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        result = []
        
        while q:
            s = len(q)
            res = []
            for _ in range(s):
                node = q.popleft()
                res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            result.append(res)
            
        return result[::-1]