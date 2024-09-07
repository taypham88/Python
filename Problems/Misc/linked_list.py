class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = linked_list.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
 
linked_list = LinkedList()
linked_list.add(Node('Alice'))
linked_list.add(Node('Chad'))
linked_list.add(Node('Debra'))
linked_list.add(Node('James'))
linked_list.add(Node('Kelley'))
linked_list.add(Node('Mark'))
linked_list.add(Node('Brian'))

node = linked_list.head
while node:
     print(node.value)
     node = node.next
