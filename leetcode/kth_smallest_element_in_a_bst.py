"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return []
            return [*inorder(root.left), root.val, *inorder(root.right)]

        return inorder(root)[k-1]

# or

class Solution:
    def __init__(self):
        self.res = None
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        
        def find_kth_smallest_elm(root, k):
            if root:
                find_kth_smallest_elm(root.left, k)
                k[0]-=1
                if k[0] == 0:
                    
                    self.res = root.val
                find_kth_smallest_elm(root.right, k)
                    
                
            else:
                return
        
        
        find_kth_smallest_elm(root, [k])
        return self.res
           
        