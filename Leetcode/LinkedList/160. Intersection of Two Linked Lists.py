# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curA = headA
        visited = set()
        while curA != None:
            visited.add(curA)
            curA = curA.next
            
            
        curB = headB
        while curB != None:
            if curB in visited:
                return curB
            
            curB = curB.next
            
        return None
    
    
    class AlthernateSolution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            lenA = 0
            lenB = 0
            currA = headA
            currB = headB
            
            while currA:
                lenA += 1
                currA = currA.next
                
            while currB:
                lenB += 1
                currB = currB.next
                
                
            diff = abs(lenA - lenB)
            
            currA = headA
            currB = headB
            
            while diff > 0:
                if lenA > lenB:
                    currA = currA.next
                else: 
                    currB = currB.next
                    
                diff -= 1
                
            while currA or currB:
                if currA == currB:
                    return currA
                currA = currA.next
                currB = currB.next
                
            return None
            