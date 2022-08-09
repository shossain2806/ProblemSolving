import Foundation


fileprivate class ListNode {
    fileprivate var val: Int
    fileprivate var next: ListNode?
    fileprivate init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}


fileprivate class Solution {
    func detectCycle(_ head: ListNode?) -> ListNode? {
        guard head != nil else {
            return head
        }
        
        var slower: ListNode? = head
        var faster: ListNode? = head
        var meet: ListNode?
        while slower != nil && faster != nil {
            slower = slower?.next
            faster = faster?.next?.next
            if slower === faster {
                meet = slower
                break
            }
            
        }
        guard let meetNode = meet else {
            return nil
        }
        slower = head
        faster = meetNode
        while slower !== faster {
            slower = slower?.next
            faster = faster?.next
        }
        return slower
    }
}
