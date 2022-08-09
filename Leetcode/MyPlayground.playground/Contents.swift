import UIKit

//func printAllNodes<Element>(_ head: SingleLinkedList<Element>) {
//    var curr : SingleLinkedList<Element>?
//
//    curr = head
//
//    while curr != nil {
//        if let curr = curr {
//            print(curr.value)
//        }
//
//        curr = curr?.next
//    }
//}
//
//let values = [23, 6, 15]
//var head: SingleLinkedList<Int>?
//var curr: SingleLinkedList<Int>?
//
//
//for value in values {
//    let node = SingleLinkedList<Int>(value: value)
//    guard head != nil else {
//        head = node
//        curr = node
//        continue
//    }
//    if let curr = curr {
//        curr.next = node
//    }
//
//    curr = node
//}
//
//if let headUnwr = head {
//    printAllNodes(headUnwr)
//}
//
//
//// insert in beginning
//print("Insert in the beginning....")
//let node = SingleLinkedList<Int>(value: 18)
//node.next = head
//head = node
//
//if let headUnwr = head {
//    printAllNodes(headUnwr)
//}
//
//// delete
//
////
//for i in 0...5 {
//    print(i)
//}
        
let sol = Solution()
sol.construct()
print(sol.hasCycle(sol.mainHead))
