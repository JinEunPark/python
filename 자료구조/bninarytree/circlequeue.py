class circleQueue:

    def __init__(self):
        self.queue = [None]*10
        self.front = 0
        self.tail = 0
        self.max = 10
    def isFull(self):
        return self.front == (self.tail +1)%self.max

    def isEmpty(self):
        return self.front == self.tail

    def enquene(self, data):
        if not self.isFull():
            self.tail = (self.tail + 1) % self.max
            self.queue[self.tail] = data

    def dequene(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max
            return self.queue[self.front]
