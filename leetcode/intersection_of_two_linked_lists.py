"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        len_A = len_B = 1
        A = headA
        while A:
            A = A.next
            len_A+=1
        B=headB     
        while B:
            B = B.next
            len_B+=1
        
        if len_A > len_B:
            for i in range(len_A-len_B):
                headA = headA.next
        elif len_A < len_B:
            for i in range(len_B-len_A):
                headB = headB.next
        
        while headA != headB:
            headA=headA.next
            headB = headB.next
        return headA
        
        
        