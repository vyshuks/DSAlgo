"""
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.max_depth = -1
        self.result_node = TreeNode()
        self.find_lowest_common_ancestor(root, 0)
        return self.result_node
    
    def find_lowest_common_ancestor(self, node, depth):
        if not node:
            return depth
        
        
        left = self.find_lowest_common_ancestor(node.left, depth+1)
        right = self.find_lowest_common_ancestor(node.right, depth+1)
        
        if left==right:
            self.max_depth = max(self.max_depth, left)
            if self.max_depth == left:
                self.result_node = node
                
                
        return max(left, right)
        