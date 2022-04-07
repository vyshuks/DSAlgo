"""
https://leetcode.com/problems/valid-palindrome-ii/
"""

def is_palindrome(s: str, i: int, j: int) -> bool:
    while i <= j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

def valid_palindrome(s: str) -> bool:
    str_len = len(s)
    left_ptr, right_ptr = 0, str_len-1

    while left_ptr <= right_ptr:
        if s[left_ptr] == s[right_ptr]:
            left_ptr+=1
            right_ptr-=1
        else:
            return is_palindrome(s, left_ptr+1, right_ptr) or is_palindrome(s, left_ptr, right_ptr-1)
    return True

print(valid_palindrome('aba'))