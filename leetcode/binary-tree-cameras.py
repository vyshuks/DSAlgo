"""
https://leetcode.com/problems/binary-tree-cameras/
"""

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.no_of_camera = 0
        def dfs(node):
            if not node:
                return False, True
            
            c1,m1 = dfs(node.left)
            c2,m2 = dfs(node.right)
            
            camera, monitor = False, False
            
            if c1 or c2:
                monitor = True
            
            if not m1 or not m2:
                camera = True
                self.no_of_camera+=1
                monitor = True
                
            return camera, monitor
        
        c,m = dfs(root)
        return self.no_of_camera if m else self.no_of_camera+1