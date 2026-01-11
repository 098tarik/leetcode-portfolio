class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def pop_front(self):
        result = None
        if self.head:
            result = self.head.val
            self.head = self.head.next
        self.size -= 1
        return result
    
    def push_back(self,val):
        self.size += 1
        if not self.head:
            self.head = Node(val)
            return
        curr_node = self.head

        while curr_node:
            curr_node = curr_node.next
        
        curr_node = Node(val)

