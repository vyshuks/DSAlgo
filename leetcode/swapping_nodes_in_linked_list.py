"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1 = n2 = None
        p  = head
        
        while p:
            k-=1
            n2 = None if n2 is None else n2.next    
            
            if k==0:
                n1=p
                n2=head
            
            p = p.next
        
        if n1 and n2:
            n1.val, n2.val = n2.val, n1.val
        
        return head