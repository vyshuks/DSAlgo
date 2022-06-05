"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        
        
        cur = head
        while cur:
            if cur.random:
                tmp = cur.next
                tmp.random = cur.random.next
            cur=cur.next.next
        
        old = head
        new = dummy = Node(-1)
        # new =t1
        # old = new.next
                           
        while old:
            new.next = old.next
            new = old
            old = new.next
        return dummy.next