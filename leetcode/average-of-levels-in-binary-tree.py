"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        result = []
        
        while q:
            
            s = len(q)
            tot = 0
            for _ in range(s):
                node = q.popleft()
                tot+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(tot/s)
        return result