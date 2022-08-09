import Foundation

fileprivate class DLLNode {
   
    let value: Int
    var next: DLLNode?
    
    init(value: Int) {
        self.value = value
    }
}

public class MyLinkedList {
    fileprivate var head: DLLNode?

    
    public init() {
        
    }
    
    public func get(_ index: Int) -> Int {
        var count = 0
        var cur = head
        while cur != nil {
            if count == index {
                return cur?.value ?? -1
            }
            cur = cur?.next
            count += 1
        }
        return -1
    }
    
    public func addAtHead(_ val: Int) {
        let node = DLLNode(value: val)
        
        if let head = head {
            node.next = head
            self.head = node
        }
        else {
            self.head = node
        }
        
    }
    
    public func addAtTail(_ val: Int) {
        let node = DLLNode(value: val)
        var curr = head
        guard curr != nil else {
            addAtHead(val)
            return
        }
        while curr?.next != nil {
            curr = curr?.next
        }
        curr?.next = node
    }
    
    public func addAtIndex(_ index: Int, _ val: Int) {
        var count = 0
        var cur: DLLNode? = head
        var prev: DLLNode?
        let node = DLLNode(value: val)
        if index == 0 {
            addAtHead(val)
            return
        }
            
        while cur != nil {
            if count == index {
                if index == 0 {
                    addAtHead(val)
                } else {
                    prev?.next = node
                    node.next = cur
                }
                return
            }
            prev = cur
            cur = cur?.next
            count += 1
        }
        
        if count == index {
            addAtTail(val)
        }
    }
    
    public func deleteAtIndex(_ index: Int) {
        var count = 0
        var cur: DLLNode? = head
        var prev: DLLNode?
        while cur != nil {
           
            if count == index {
                if index == 0 {
                    head = head?.next
                } else {
                    prev?.next = cur?.next
                }
                return
            }
            prev = cur
            cur = cur?.next
            count += 1
        }
    }
    
}
