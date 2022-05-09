class decQueue:

    def __init__(self):
        self.decQueueSize = 10
        self.list = [None] * 10
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.decQueueSize

    def addFront(self, item):
        result = self.isFull == False
        if result:
            self.list[self.front] = item
            self.front = (self.front - 1 + self.decQueueSize) % self.decQueueSize

    def deleteFront(self):

        if self.isEmpty == False:
            out = self.list[self.front + 1]
            self.front = (self.front + 1) % self.decQueueSize
            return out

    def getFront(self):
        if self.isEmpty() == False:
            return self.list[(self.front - 1 + self.decQueueSize) % self.decQueueSize]

    def addRear(self, item):
        result = self.isFull() == False
        if result:
            self.rear = (self.rear + 1) % self.decQueueSize
            self.list[self.rear] = item

    def deleteRear(self):
        if self.isEmpty == False:
            out = self.list[self.rear]
            self.rear = (self.rear - 1 + self.decQueueSize) % self.decQueueSize
            return out

    def getRear(self):
        if self.isEmpty() == False:
            return self.list[self.rear]

    def size(self):
        return (self.rear - self.front + self.decQueueSize) % self.decQueueSize

    def display(self):
        if self.front > self.rear:
            print(self.list[self.front + 1: self.decQueueSize] + self.list[0:self.rear + 1])
        else:
            print(self.list[self.front + 1:self.rear + 1])

    def clear(self):
        self.list = []


dp = decQueue()
for i in range(9):
    if i % 2 == 0:
        dp.addRear(i)
    else:
        dp.addFront(i)
print(dp.list)
dp.display()
