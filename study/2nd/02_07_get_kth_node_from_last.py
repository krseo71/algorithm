class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # def get_kth_node_from_last(self, k):
    #     length = 1
    #     cur = self.head
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #     end_length = length - k
    #     cur = self.head
    #     for i in range(end_length):
    #         cur = cur.next
    #     return cur
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow
