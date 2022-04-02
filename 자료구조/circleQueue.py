class circleQueue:

    def __init__(self):
        self.MAXQ = 10
        self.list = [None] * self.MAXQ  # MAXQ사이즈의 비어있는 리스트 생성함.
        self.front = 0
        self.rear = 0
        # class 에서는 항상 변수 선언을 생성자 안에서 조져야지 클래스
        # 변수가 되는거야 진은아.

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1)

    def dequeue(self):
        if self.isEmpty() == False: # 다운플로우 막기 위해서 실행해준다.
            self.front = (self.front + 1) % self.MAXQ  # front 변수가 앞으로 이동하기
            return self.list[self.front]
            # 때문에 list안에 있는 변수를 삭제할 필요가 없어 진은아

    def enqueue(self, item):
        if self.isFull() == False: #오플로우를 막기 위해서 실행해준다.
            self.rear = (self.rear + 1) % self.MAXQ
            self.list[self.rear] = item
            # 여기서 insert연산 사용하면 파이썬은 리스트가 동적할당이라 리스트 크기가 커진다 진은아 조심해
            # MAXQ로 나눠주는 이유는
            # 순환적으로 돌아야되기 때문이야 진은아 만약에 rear  가 10 이 되면
            # 다시 0번으로 자료를 삽입해야지 진은아

    def peek(self):
        return self.list[(self.front + 1) % self.MAXQ]

    def size(self):
        return (self.front - self.rear + self.MAXQ) % self.MAXQ

    def display(self):
        if self.front > self.rear:
            print("f {}, r{}".format(self.front, self.rear),
                  self.list[self.front + 1:self.MAXQ] + self.list[0:self.rear + 1])
        else:
            print("f {} , r{}".format(self.front, self.rear), self.list[self.front + 1:self.rear + 1])

