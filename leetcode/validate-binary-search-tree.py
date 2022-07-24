"""
https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left_bound, node, right_bound):
            if not node:
                return True
            
            if node.val <= left_bound or node.val >= right_bound:
                return False
            
            return dfs(left_bound, node.left, node.val) and dfs(node.val, node.right, right_bound)
        
        return dfs(float('-inf'), root, float('inf'))
        