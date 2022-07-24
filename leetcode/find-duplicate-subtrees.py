"""
https://leetcode.com/problems/find-duplicate-subtrees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        
        tree_map = {}
        
        def dfs(root, path):
            if not root:
                return '#'
            
            path += ",".join([str(root.val), dfs(root.left, path), dfs(root.right, path)])
            
            if path in tree_map:
                tree_map[path]+=1
                if tree_map[path]==2:
                    res.append(root)
            else:
                tree_map[path] = 1
                
            return path
        
        dfs(root, '')
        return res
        