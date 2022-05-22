"""
https://leetcode.com/problems/palindromic-substrings/
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        if n==1:
            return 1;
        ans = 0
        
        def check_pal(left,right):
            if left > right:
                return 0
            count = 0
            print(left,right)
            while (left >=0 and right < n) and (s[left] == s[right]):
                count+=1
                left-=1
                right+=1
                
            return count
        
        for i in range(n):
            ans+=check_pal(i,i)
            ans+=check_pal(i,i+1)
        

        
        return ans