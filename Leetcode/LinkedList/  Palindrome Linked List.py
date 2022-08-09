# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head:
            return True
        
        # find mid
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # rev last part
        node = slow.next
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        slow.next = prev  
        node = slow.next
        while node and head.val == node.val:
            head = head.next
            node = node.next
            
        return node == None
    
    
    
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(Solution().isPalindrome(node1))