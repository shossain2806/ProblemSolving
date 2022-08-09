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
    
    public func hasCycle(_ head: ListNode?) -> Bool {
        guard  head != nil else {
            return false
        }
        var slower : ListNode? = head
        var faster: ListNode? = head
        
        while slower != nil && faster != nil {
            slower = slower?.next
            faster = faster?.next?.next
            if slower === faster && (slower != nil || faster != nil) {
                return true
            }
        }
        return false
    }
}

//[3,2,0,-4]
