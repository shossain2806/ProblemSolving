import Foundation

fileprivate class Node<Element> {
    fileprivate let value: Element
    fileprivate var next: Node?
    
    public init(value: Element) {
        self.value = value
    }
    
}


fileprivate class SingleLinkedList<Element> {
    
    fileprivate var head: Node<Element>?
    fileprivate var current: Node<Element>?
    
    init(values: [Element]) {
        for value in values {
            let node = Node<Element>(value: value)
            guard head != nil else {
                head = node
                current = node
                continue
            }
            if let curr = current {
                curr.next = node
            }
            
            current = node
        }
    }
    
    func insertAt(_ index: inout Int, value: Element) {
        var curr = head
        while index > 0 {
            if let current = curr {
                curr = current.next
            }
            index -= 1
        }
        let node = Node<Element>(value: value)
        node.next = curr
        
//        cur
    }
}
