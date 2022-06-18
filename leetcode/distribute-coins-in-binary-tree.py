"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.step = 0
        
        def dfs(parent, child):
            if not child:
                return
            
            dfs(child, child.left)
            dfs(child, child.right)
            
            if child.val > 1:
                excesscoins = child.val-1
                child.val = 1
                parent.val+=excesscoins
                self.step+=excesscoins
            elif child.val < 1:
                neededcoin = 1+abs(child.val)
                child.val = neededcoin
                parent.val -= neededcoin
                self.step+=neededcoin
                
            
        dfs(root, root)
        return self.step