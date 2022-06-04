"""
https://leetcode.com/problems/simplify-path/
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        
        p = [i for i in p if i != ""]
        stack = []
        
        for c in p:
            if c==".":
                continue
            elif c=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "/"+"/".join(stack)
        
        
        