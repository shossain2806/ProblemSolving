# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        tip = head
        prev = None
        while n > 1:
            tip = tip.next  
            n -= 1
            
            
        while tip.next:
            prev = curr
            tip = tip.next
            curr = curr.next
            
        if not prev:
            head = head.next
        else:    
            prev.next = curr.next
            
        return head