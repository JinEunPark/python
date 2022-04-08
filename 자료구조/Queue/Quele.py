class Queue:
    def __init__(self):
        self.maxQ = 10
        self.list = [None] * self.maxQ
        self.front = 0
        self.rear = 0

    def isFull(self):
        return self.front == (self.rear + 1) % self.maxQ

    def peek(self):
        if not self.isEmpty():
            return self.list[self.rear]

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.maxQ
            self.list[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxQ
            return self.list[self.front]

    def clear(self):
        self.front == self.rear

    def isEmpty(self):
        return self.rear == self.front

    def size(self):
        return (self.front - self.rear + self.maxQ) % self.maxQ

    def display(self):
        if self.rear > self.front:
            self.list[self.front + 1:self.rear + 1]
        else:
            self.list[(self.front + 1) % self.maxQ:self.maxQ] + self.list[0:(self.rear + 1) % self.maxQ]


def fibonacci(c):
    Q = Queue()
    Q.enqueue(0)
    Q.enqueue(1)
    if c == 1:
        return 1
    elif c == 0:
        return 0

    for i in range(c):
        b = Q.peek()
        a = Q.dequeue()

        Q.enqueue(a + b)
    return Q.dequeue()


def fido(c):
    if c ==1 :
        return 1
    elif c == 0:
        return 0
    f_1 = 1
    f_0 = 0
    for i in range(c-1):
        f_2 = f_1 + f_0
        f_0 = f_1
        f_1 = f_2
    return f_2



print(fido(5))
print(fibonacci(5))
