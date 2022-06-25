"""
https://leetcode.com/problems/restore-the-array/
"""

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        self.memo = {}
        def helper(s,i,k):
            if i == len(s):
                return 1
            if i in self.memo:
                return self.memo[i]
            if s[i] == '0':
                return 0
            ans = 0
            num = 0
            for j in range(i, len(s)):
                num = num*10 + int(s[j])
                if num > k:
                    break
                ans += helper(s, j+1, k)
                ans = ans%(10**9 + 7)
            self.memo[i] = ans
            return ans
                
        return helper(s,0,k)
        