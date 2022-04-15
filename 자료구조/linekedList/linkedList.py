from Node import node as Node
import random as random


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insert(self, pos, value):
        before = self.getNode(pos - 1)
        if before == None:
            if self.isEmpty():
                self.head = Node(value, self.head)
            else:
                node = Node(value, self.head)
                self.head = node
        else:
            before.link = Node(value, before.link)

    def size(self):
        count = 0
        node = self.head
        while node is not None:
            node = node.link
            count += 1
        return count

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before is None:
            if self.isEmpty():
                return None
            else:
                data = self.head
                self.head = self.head.link
                return data
        elif before is not None:
            data = before.link.data
            before.link = before.link.link
            return data

    def getNode(self, pos):

        if pos < 0:
            return None

        node = self.head
        while pos > 0 and node is not None:
            node = node.link
            pos -= 1
        return node

    def sorting(self, answer: bool):

        if answer == True:
            for i in range(self.size() - 1, 0, -1):

                beChanged = False

                node = self.head
                for e in range(i):

                    if node.data > node.link.data:
                        node.data, node.link.data = node.link.data, node.data
                    node = node.link

    def display(self):
        node = self.head
        while node is not None:
            print(node.data, end="->")
            node = node.link
        print("None")


la = LinkedList()
for i in range(5):
    la.insert(la.size(),int(random.random()*10))
la.display()

la.sorting(True)
la.display()
