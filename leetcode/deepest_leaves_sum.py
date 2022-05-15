"""
https://leetcode.com/problems/deepest-leaves-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        levelsum = 0
        while q:
            
            s = len(q)
            levelsum = 0
            for _ in range(s):
                node = q.popleft()
                levelsum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return levelsum