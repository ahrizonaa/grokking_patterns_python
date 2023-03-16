
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val) -> None:
        node = Node(val)
        self.head = node
        self.tail = node
        self.length = 1
    def append(self, val):
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    def pop(self):
        pass
    def push(self):
        pass
    def print(self):
        tmp = self.head
        s = ''
        while tmp is not None:
            s += str(tmp.val)
            tmp = tmp.next
            if tmp is not None:
                s += ' > '
        print(s)

llist = LinkedList(4)
llist.append(6)
llist.append(8)

llist.print()