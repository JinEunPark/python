from collections import deque
class dacQue:
    def __init__(self):
        self.max = 10
        self.list = [None] * 10
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.max

    def addFront(self, item):
        if self.isFull() == False:

            self.list[self.front] = item
            self.front = (self.front - 1 + self.max) % self.max


    def __str__(self):
        return str(self.list)


qu = dacQue()
for i in range(5):
    print(qu.isFull())
    qu.addFront(i)

print(qu)
