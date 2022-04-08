from circleQueue import circleQueue  # 같은 디랙토리 안에 있어야 임포트 문을사용할 때 오류가 발생하지 않는다.


class deQueue(circleQueue):
    def __init__(self):
        super().__init__()  # 상속받은 생성자를 실행시켰다.

    def addRear(self, item):
        if not self.isFull():
            self.enqueue(item)

    def delelteRear(self):
        if not self.isEmpty():
            re = self.list[self.rear]
            self.rear = (self.rear - 1 + self.MAXQ) % self.MAXQ
            return re

    def getRear(self):
        return self.list[self.rear]

    def deleteFront(self):
        if not self.isEmpty():
            return self.dequeue()

    def addFront(self, item):
        if not self.isFull():
            self.list[self.front] = item
            self.front = (self.front - 1 + self.MAXQ) % self.MAXQ

    def getFront(self):
        return self.list[(self.front + 1) % self.MAXQ]

    def isEmpty(self):
        self.isEmpty()

    def isFull(self):
        self.isEmpty()


