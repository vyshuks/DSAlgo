"""
https://leetcode.com/problems/increasing-order-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dummy = TreeNode()
        self.ans = self.dummy
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        
        def helper(root):
            if root:
                helper(root.left)
                root.left = None
                self.dummy.right = root
                self.dummy = root
                helper(root.right)
            else:
                return
        
        helper(root)
        return self.ans.right