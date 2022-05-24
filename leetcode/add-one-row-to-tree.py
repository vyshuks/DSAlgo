"""
https://leetcode.com/problems/add-one-row-to-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, l, d):
            if not node:
                return None
            elif d==1:
                return TreeNode(val, left=node)
            elif l==d-1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
                return node
            dfs(node.left, l+1,d)
            dfs(node.right, l+1,d)
            return node
            
        return dfs(root, 1, depth)
                
                    
            
            
        