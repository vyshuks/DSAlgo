"""
https://leetcode.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        
        def reverse(head):
            nxt, prev, cur = None, None, head
            
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        cur = head
        mid = head
        while cur and cur.next:
            cur = cur.next.next
            mid = mid.next
        
        
        first = head
        second = reverse(mid)
        
        
        while first and second:
            
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True
        