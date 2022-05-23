"""
https://leetcode.com/problems/ones-and-zeroes/
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def helper(s, m, n, i,memo):
            if (m,n,i) in memo:
                return memo[(m,n,i)]
            
            if i==len(s):
                return 0
            
            count_zero = s[i].count('0')
            count_one = s[i].count('1')
            consider=0
            if m-count_zero >=0 and n-count_one >=0 and i<len(s):
                consider = helper(s,m-count_zero,n-count_one,i+1, memo)+1
            not_consider = helper(s,m,n,i+1, memo)
            memo[(m,n,i)]=max(consider, not_consider)
            return memo[(m,n,i)]
            
        return helper(strs,m,n,0, memo)
        