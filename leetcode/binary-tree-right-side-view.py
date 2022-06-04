"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        
        def dfs(node, height):
            if not node:
                return
            if height not in d:
                d[height]=node.val
            dfs(node.right, height+1)
            dfs(node.left, height+1)
        
        dfs(root, 0)
        return d.values()
            
        