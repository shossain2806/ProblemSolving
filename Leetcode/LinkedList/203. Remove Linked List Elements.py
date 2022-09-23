# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        cur = head
        prev = None
        
        while cur:
            if cur.val == val:
                if not prev:
                    head = head.next
                    cur = head
        
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
            
        return head

node1 = ListNode(7)
node2 = ListNode(7)
node3 = ListNode(7)
node4 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1    
sol = Solution()
sol.removeElements(head, 7)
