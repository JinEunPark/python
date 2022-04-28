from 자료구조.장_6.node import node as Node


class linkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            self.head = self.head.link
            return data

    def peek(self):
        if not self.isEmpty():
            return self.head.data

    def size(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.link
        return count

    def display(self):
        node = self.head
        while node != None:
            print(node.data, end="=>")
            node = node.link
        print("none")


linklist = linkedList()
for i in range(10):
    linklist.push(i)
linklist.display()
for i in range(5):
    linklist.pop()
linklist.display()
