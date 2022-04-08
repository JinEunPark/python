from node import node


class linkedStack:

    def __init__(self):
        self.top = None  # 헤드 포인터 원래 첫번째 요소랑 연결되어있음

    def isEmpty(self):
        return self.top == None

    def clear(self):
        self.top = None

    def push(self, data):
        # if self.top != None:
            self.top = node(data, self.top)  # 원래top 랑 연결되어있는 연결을 새로운 노드를 생성하면서
        # 새로운 노드가 원래 첫번째 요소를 연결되게 만든다.
        # else:
        #     self.top = node(data, None)

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
        else:
            return None

    def peek(self):
        return self.top.data

    def size(self):
        start = self.top
        count = 0
        while start != None:
            start = start.link
            count += 1
        return count

    def display(self):
        if self.top == None:
            return None
        else:
            start = self.top
            while start != None:
                print(start.data, end="->")
                start = start.link
        print()


ls = linkedStack()
for i in range(10):
    ls.push(i)
ls.display()
for i in range(3):
    print(ls.pop(), end="=>")
print()
ls.display()
