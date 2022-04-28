class circleQueue:
    def __init__(self):
        self.items = []
        self.rear = 0
        self.front = 0
        self.max = 10

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return (self.rear + 1) % self.max == self.front

    def clear(self):
        self.rear = self.front

    def enquene(self, item):
        if not self.isEmpty():
            self.items[self.rear] = item
            (self.rear + 1) % self.max

    def dequeue(self):
        data = self.items[(self.front + 1) % self.max]
        self.front = (self.front + 1) % self.max
        return data

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.max]

    def size(self):
        return (self.rear - self.front + self.max) % self.max  # 이거 존나 나올거 같에 진은아 그러니까 제발 내일 시험 보기 직전에 한변보고가자

    def display(self):
        if self.raer > self.front:
            return self.items[
                   self.front + 1: self.raer + 1]  # 이렇게 까지만 작성해줘도 상관없어 진은아 왜냐하면 이건 말이다 어차피 레어가 더 크다는 가정하에 하고
            # 하고 있는 거기 때무이야 진은아 제발 쓸데없느 ㄴ걸로 신경쓰지마 진은아 제발 아니 존나 졸리다 시발 집에가서 퍼질러 자고 시ㅏㅍ어 시발
            # return self.items[(self.front + 1) % self.max: (self.raer + 1) % self.max] 이건 니 생각이고 진은아 사실 이렇게 까지하지 않아도 충분히 가능하단다
        else:
            return self.items[self.front + 1: self.max] + self.items[
                                                          0:self.raer + 1]  # 여기서도 모둘레이션하지 않아도 존나 작동자라한다 진은아 걱정하지마 제바
            # return self.items[(self.front + 1) % self.max: self.max] + self.items[0: (self.rear + 1) % self.max]

        # 덱을 만들기 위해서는 추가해야할 연산들이 있느데 그게 바로  addfront  delete rear 야 그러니가 이거 두개는 확실하게 기억두자 진은아 박진은아 제발

    def addFront(self, item):
        self.items[self.front] = item
        self.front = (self.front - 1 + self.max) % self.max

    def deleterear(self):
        data = self.items[self.raer]
        self.rear = (self.rear - 1 + self.max) % self.max
        return data

    def findmaxindex(self): # 이거는 정려되지 않은 우선순위큐를 구현하고 출력할때 인덱스를 찾아서 반납할 때 사용하는 메서드야 진은아 제발 기억좀하자 진은아 제랍 남산위
        maxindex = 0
        for i in range(len(self.items)):
            if self.items[maxindex] < self.items[i]:
                maxindex = i
        return maxindex
