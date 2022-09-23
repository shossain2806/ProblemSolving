class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        slower = head
        faster = head.next
        
        while slower != faster:
            if faster is None or faster.next is None:
                return False
            
            slower = slower.next
            faster = faster.next.next
            
        return True