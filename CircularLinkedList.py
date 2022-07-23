class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList(object):
    def __init__(self, node=None):
        self.head: Node = node
        if node:
            node.next = node

    def is_empty(self):
        return self.head is None

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
            return

        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = node
        node.next = self.head

    def search(self, item):
        # empty
        if self.is_empty():
            return None
        # more than one element
        cur = self.head
        while cur.next != self.head:
            if cur.data == item:
                return cur
            cur = cur.next
        # only one element
        if cur.data == item:
            return cur
        return None

    def search(self, item):
        # empty
        if self.is_empty():
            return None
        # more than one element
        cur = self.head
        while cur.next != self.head:
            if cur.data == item:
                return cur
            cur = cur.next
        # only one element
        if cur.data == item:
            return cur
        return None