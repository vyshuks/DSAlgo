"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.max_depth = -1
        self.result = TreeNode()
        self.find_deep_subtree(root, 0)
        return self.result
    
    def find_deep_subtree(self, node, depth):
        if not node:
            return depth
        
        left_depth = self.find_deep_subtree(node.left, depth+1)
        right_depth = self.find_deep_subtree(node.right, depth+1)
        
        if left_depth == right_depth:
            self.max_depth = max(self.max_depth, left_depth)
            if left_depth==self.max_depth:
                self.result = node
        
        return max(left_depth, right_depth)
                
        