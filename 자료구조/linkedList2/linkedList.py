from node import node as Node


class linkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        if not self.isEmpty():
            start = self.head
            count = 0
            while start != None:
                start = start.link
                count += 1
            return count
        else:
            return 0

    def display(self, msg="linkedlist"):

        start = self.head
        print(msg, end=":")
        if self.isEmpty():
            print("None")
        while start != None:
            print(start.data, end=" ->")
            start = start.link
        print("None")

    def getNode(self, pos):
        if pos < 0:
            return None
        else:
            node = self.head
            while pos > 0 and node != None:
                node = node.link
                pos -= 1
            return node

        # if self.isEmpty():
        #     return None
        # index = 0  # 시작하는 index = 0
        # node = self.head
        # while index != pos:
        #     node = node.link
        #     index += 1
        # return node

    def getEntry(self, pos):  # pos에 있는 노드의 데이터 반환
        if not self.isEmpty():
            node = self.head
            while pos > 0 and node != None:  # 주어진 인덱스 번 연사을 해야한다
                node = node.link
                pos -= 1
            return node.data

    def replace(self, pos, elem):  # pos 에 있는 data 를 elem으로 교체
        if pos < 0:
            return None
        else:
            node = self.head
            while pos > 0 and node != None:
                node = node.link
            node.data = elem  # pos 의 위치에 있는 node를 교체함

    def find(self, value):  # value 를 가진 node의 인덱스를 반환
        node = self.head
        while node.data != value:
            node = node.link
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:  # pos -1 이 0 보다 작다는 거고 그러면 pos 가 0이라는거
            if self.head == None:  # head가 가르키는 노드가 없고 처음 삽입하는 거지
                self.head = Node(elem, None)  # 처음이자 마지막 노드를 생성
            else:
                self.head = Node(elem, self.head.link)
        else:
            # pos -1 .link 를 link 로 가지는 새로운 node 생성
            before.link = Node(elem, before.link)  # 이 새로 pos 다음의 노드와 연결된거임

    def delete(self, pos):  # pos에 있는 노드 삭제
        if self.isEmpty():
            return
        else:
            before = self.getNode(pos - 1)  # 삭제하려는 전노를 찾음
            if before == None:  # 노가의 index가 0이라서 getNode(pos -1) 을 실행하면 None 을 반환하니까 None이면 첫번째 node를 삭제하라고 한거임
                self.head = self.head.link
            else:
                before.link = before.link.link


s = linkedList()
s.display()
for i in range(10):
    s.insert(i, i * 10)
s.display()
s.insert(s.size(),1000)
s.display()
for i in range(5):
    s.delete(i)
s.display()
s.delete(-5)
s.display()