"""
https://leetcode.com/problems/partition-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small , large = ListNode(-1), ListNode(-1)
        
        smallHead = small
        largeHead = large
        
        
        
        cur = head
        
        while cur:
            
            if cur.val < x:
                small.next = cur
                small = small.next
                
            else:
                large.next = cur
                large = large.next
            
            cur = cur.next
        
        
        large.next = None
        small.next = largeHead.next
        
        return smallHead.next