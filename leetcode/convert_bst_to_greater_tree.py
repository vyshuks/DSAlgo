"""
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.sum = 0
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val=self.sum
            self.convertBST(root.left)
        return root