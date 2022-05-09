MAX_QSIZE = 10


# 큐의 프론트는 가장 앞에 있는 데이터의 하나 인덱스 전에ㅐ 있는 거임
# 데이터의 삽입은 숫자가 증가하는 방향으로 일어난다.
# front 는 첫번째 데이터 하나전의 인덱스
# rear 는 마지막 데이터가 존재하는 인덱스

class CircularQ:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear  # 큐가 비워졌을 땨

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE  # Q 사이즈의 나머지가

    def clear(self):
        self.front = self.rear  # 포인터만 바꿔서 메모리 릴리즈를 따로 할필요가 없음

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = e

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front) % MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front:self.rear]
        else:
            out = self.items[self.front:MAX_QSIZE] + self.items[0:self.rear + 1]

        print("[f = {}, rear = {}]\t".format(self.front, self.rear), out)


Q = CircularQ()
print(Q.items)
for i in range(7): Q.enqueue(i)
Q.display()
print(Q.items)

for i in range(6): Q.dequeue()
Q.display()
print(Q.items)

for i in range(5): Q.enqueue(i)
Q.display()
print(Q.items)

