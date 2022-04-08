"""
https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        left_ptr = 0
        right_ptr = l-1
        
        while left_ptr < right_ptr:
            while left_ptr < right_ptr and not s[left_ptr].isalnum():
                left_ptr+=1
            while left_ptr< right_ptr and not s[right_ptr].isalnum():
                right_ptr-=1
            
            if s[left_ptr].lower() != s[right_ptr].lower():
                return False
            left_ptr+=1
            right_ptr-=1
            
        return True