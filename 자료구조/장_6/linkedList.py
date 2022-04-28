from 자료구조.장_6.node import node as Node


class linkedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0:
            return None
        else:
            node = self.head

            while pos > 0 and node != None:
                node = node.link
                pos -= 1
            return node

    def getEntyry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, data):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            node.data = data

    def find(self, data):
        node = self.head

        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return node  # 못찾으면 none을 반환한다 위에서 while문이 node 가 none일때 멈추니까 이거 반환하면 none 되느니거야 진은아

    def insert(self, pos, item):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(item, self.head)  # 가장 삽입하는 경우엔 self.head에 있던 none을 삽입해서  연결을만들어 준다.
        else:
            before.link = Node(item, before.link)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if self.head != None:
                self.haed = self.head.link
        elif before != None:
            before.link = before.link.link

        # if self.isEmpty():
        #     return None
        # else:
        #     before = self.getNode(pos - 1)
        #     if before == None:
        #         data = self.head.node.data
        #         self.head = self.head.link
        #     elif before != None:
        #         data = before.link.data
        #         before.link = before.link.link
        #         return data

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

    def display(self, mag="linkedList"):
        node = self.head
        print(mag, end="")
        while node != None:
            print(node.data, end=" , ")
            node = node.link
