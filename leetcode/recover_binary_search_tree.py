"""
https://leetcode.com/problems/recover-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first = None
        self.end = None
        self.prev = None
        
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def mark_tree(root):
            if not root:
                return
            mark_tree(root.left)
            if self.prev:
                if root.val < self.prev.val:
                    if not self.first:
                        self.first = self.prev
                    self.end = root
            
            self.prev = root
            mark_tree(root.right)
        
        mark_tree(root)
        
        self.first.val, self.end.val = self.end.val, self.first.val
        
        
        