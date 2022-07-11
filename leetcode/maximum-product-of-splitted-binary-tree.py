"""
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs_total(node):
            if not node:
                return 0
            
            return node.val + dfs_total(node.left) + dfs_total(node.right)
        
        total = dfs_total(root)
        
        self.output = 0
        
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.output = max(self.output, (total-l)*l, (total-r)*r)
            return node.val+l+r
        
        dfs(root)
        
        return self.output % (10**9+7)
            
        