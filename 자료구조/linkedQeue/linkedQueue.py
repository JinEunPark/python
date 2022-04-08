from node import node as Node


class linkedQueue:
    def __init__(self):
        self.tail = None
        # 연결된 큐에서 tail이 rear이고 tail.link가 front 이다
        # 큐는 front에서 data의 삭제가 일어나고 rear에서 데이터의 삽입이 일어나는 구조이다.

    def isEmpty(self):
        return self.tail == None

    def clear(self):
        self.tail = None

    def peek(self):
        return self.tail.link.data

    # 큐에서 front의 data가 반환되어야한다
    def enqueue(self, data):
        # data가 처음으로 들어가는 경우
        # 자기 자신을 링크로 연결
        if self.isEmpty():
            node = Node(data, None)
            node.link = node
            self.tail = node
        else:
            node = Node(data, self.tail.link)  # link to front
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data  # 프론트의 데이터를 변수에 할당
            if self.tail.link == self.tail:  # 노드가 1개 일경우에 link가 자기 자신이므로 설정
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
        return None

    def size(self):
        count = 1
        if not self.isEmpty():
            start = self.tail.link
            while start != self.tail:
                start = start.link
                count += 1
            return count
        else:
            return 0

    def display(self, msg="linkedQueue"):
        print(msg, end=" : ")
        if self.isEmpty():
            print("None")
        elif self.tail == self.tail.link:
            print(self.tail.data)
        else:
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=" ->")
                node = node.link
            print(node.data)


Q = linkedQueue()
for i in range(10):
    Q.enqueue(i)
Q.display()

for i in range(3):
    Q.dequeue()
Q.display()
