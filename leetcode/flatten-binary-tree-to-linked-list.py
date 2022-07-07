"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return
            
            left_end = dfs(node.left)
            right_end = dfs(node.right)
            
            if left_end:
                left_end.right = node.right
                node.right = node.left
                node.left = None
                
            return right_end or left_end or node
        
        dfs(root)
       