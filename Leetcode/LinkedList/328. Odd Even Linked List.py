# # Definition for singly-linked list.
# from platform import node


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headOdd = None
        trailOdd = None
        headEven = None
        trailEven = None
        oddFlag = True
        
        while head:
            if oddFlag:
                if not headOdd:
                    headOdd = head
                    trailOdd = head
                else:
                    trailOdd.next = head
                    trailOdd = trailOdd.next
                
            else: 
                if not headEven:
                    headEven = head
                    trailEven = head
                else:
                    trailEven.next = head
                    trailEven = trailEven.next
                
            oddFlag = not oddFlag
            head = head.next
            
        if trailOdd:
            trailOdd.next = headEven
            if trailEven:
                trailEven.next = None
        
        return headOdd
    
class AlternateSolution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd = head
        even = head.next
        headEven = even
        
        # length 1 and 2
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = headEven
        return head
    
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# Solution().oddEvenList(node1)