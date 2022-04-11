from node import node as Node


class linkedQueue:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.tail == None

    def enqueue(self, item):
        node = Node(item, None)
        if self.tail == None:
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        data = self.tail.link.data
        if not self.isEmpty():
            return None
        else:
            self.tail.link = self.tail.link.link
            return data

    def display(self):

        node = self.tail.link

        while node != self.tail:
            print(node.data, end="->")
            node = node.link

        print(self.tail.data)


def getInteger():
    lq = linkedQueue()
    while True:
        n = int(input("저장할 정수를 입력하세요(종료 : -1)"))
        if n == -1:
            lq.display()
            break
        lq.enqueue(n)


getInteger()
