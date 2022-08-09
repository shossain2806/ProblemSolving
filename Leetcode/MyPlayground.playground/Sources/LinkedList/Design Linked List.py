class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:
    
    def __init__(self):
        self.head = None
  

    def get(self, index: int) -> int:
        count = 0 
        curr = self.head
        while curr and index != count:
            curr = curr.next
            count += 1
        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            
        curr.next = node
        node.prev = curr
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        count = 0
        node = Node(val)
        curr = self.head
        while curr and count != index:
            curr = curr.next
            count += 1
            
        if curr:
            node.next = curr
            node.prev = curr.prev
            if curr.prev:
                curr.prev.next = node
                curr.prev = node
                     
        else:
            if index == count:
                self.addAtTail(val)
                
        

    def deleteAtIndex(self, index: int) -> None:
        count = 0
        curr = self.head
        while curr and count != index:
            curr = curr.next
            count += 1
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            if curr == self.head:
                self.head = curr.next
                
# list = MyLinkedList()
# list.addAtHead(7)
# list.addAtHead(2)
# list.addAtHead(1)
# list.addAtIndex(3,0)
# list.deleteAtIndex(2)
# list.addAtHead(6)
# list.addAtTail(4)
# list.get(4)
# list.addAtHead(4)
# list.addAtIndex(5,0)
# list.addAtHead(6)


# list = MyLinkedList()
# list.addAtHead(1)
# list.addAtTail(3)
# list.addAtIndex(1,2)
# print(list.get(1))
# list.deleteAtIndex(0)
# print(list.get(0))


# list = MyLinkedList()
# list.addAtIndex(1, 0)
# print(list.get(0))


# list = MyLinkedList()
# list.addAtIndex(0, 10)
# list.addAtIndex(0, 20)
# list.addAtIndex(1, 30)
# print(list.get(0))