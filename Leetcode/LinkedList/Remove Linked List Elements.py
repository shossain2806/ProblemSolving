# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        currNode = head
        prev = None
        
        while currNode:
            if val == currNode.val:
                if prev == None:
                    head = head.next
                else:
                    prev.next = currNode.next   
            else:
                prev = currNode
            
            currNode = currNode.next
            
        return head