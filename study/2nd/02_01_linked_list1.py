class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first_node = Node(5)
second_node = Node(12)
first_node.next = second_node

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()
