"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = []
        level = 1
        while q:
            s = len(q)
            res = []
            for _ in range(s):
                node = q.popleft()
                res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            if level%2 == 0:
                result.append(res[::-1])
            else:
                result.append(res)
            level+=1
            
        return result