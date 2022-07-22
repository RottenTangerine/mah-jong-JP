class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList(object):
    def __init__(self, node=None):
        self.head:Node = node
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

    def find_dora(self, item):
        # empty
        if self.is_empty():
            return None
        # more than one element
        cur = self.head
        while cur.next != self.head:
            if cur.data == item:
                return cur.next.data
            cur = cur.next
        # only one element
        if cur.data == item:
            return cur.next.data
        return None


class Indicator():
    stack = {'winds': (126976, 126980),
             'dragons': (126980, 126983),
            'characters': (126983, 126992),
            'sticks': (126992, 127001),
            'dots': (127001, 127010)}
    for i, j in stack.items():
        exec(f"""{i} = CircularLinkedList()\nfor i in range{j}:\n\t{i}.append(i)""")

    def __init__(self):
        pass

    def dora(self, i):
        for suit in [self.winds, self.dragons, self.characters, self.sticks, self.dots]:
            print(suit.find_dora(i), end=', ')


if __name__ == '__main__':
    indicator = Indicator()
    indicator.dora(127009)
    print(indicator.suits)
