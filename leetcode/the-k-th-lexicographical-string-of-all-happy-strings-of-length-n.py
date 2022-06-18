"""
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        letters = ['a', 'b', 'c']
        ans = []
        visited = set()
        
        def backtrack(s):
            if len(s) == n:
                ans.append("".join(s))
                return
                
            for c in letters:
                if not s or s[-1] != c:
                    s.append(c)
                    backtrack(s)
                    s.pop()
                
        backtrack([])
        print(ans)
        
        if len(ans) < k:
            return ""
        
        return ans[k-1]
        