"""
https://leetcode.com/problems/most-frequent-subtree-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.freq_dict = {}
        self.max_freq = 0
        
        self.dfs(root)
        
        res = []
        
        for val, freq in self.freq_dict.items():
            if freq == self.max_freq:
                res.append(val)
                
        return res
    
    def dfs(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            self.freq_dict[root.val] =  self.freq_dict.get(root.val, 0) + 1
            
            self.max_freq = max(self.max_freq, self.freq_dict[root.val])
            return root.val
        
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)
        
        total = left_sum + root.val + right_sum
        
        self.freq_dict[total] =  self.freq_dict.get(total, 0) + 1
        self.max_freq = max(self.max_freq, self.freq_dict[total])
        
        return total
        
        
        
        