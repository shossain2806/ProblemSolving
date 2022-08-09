class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head, curr = None, None
        
        c = 0
        while l1 or l2 or c != 0:
            a = 0 if not l1 else l1.val
            b = 0 if not l2 else l2.val
            
            sum = a + b + c
            c = int(sum / 10)
            
            node = ListNode(val=sum%10)
            
            if not head:
                head = node
                
            if curr:
                curr.next = node
            curr = node
            
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        

            
        return head