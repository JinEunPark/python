class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def pop(self):
        return self.top.pop()

    def push(self, item):
        self.top.append(item)


class QueueWithStack(Stack):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.Front = 0
        self.rear = 0

    def enqueue(self, item):

        self.stack1.push(item)

    def isEmpty(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            return True
        else:
            False

    def dequeue(self):

        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                item = self.stack1.pop()
                self.stack2.push(item)  # 출력을 담당하는 스택 2이 비어있다면 스택 1의 모든 내용물을 스택 2 로 옮긴다.

            return self.stack2.pop()
        else:
            return self.stack2.pop()


sQ = QueueWithStack()
for i in range(10):
    sQ.enqueue(i)
for i in range(5):
    print(sQ.dequeue(), end='->')
for i in range(11, 15):
    sQ.enqueue(i)
print(sQ.stack1.top, sQ.stack2.top)
