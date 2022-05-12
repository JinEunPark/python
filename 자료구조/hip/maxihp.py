class MaxHip:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def parent(self, i):
        return self.heap[i // 2]

    def Left(self, i):
        return self.heap[i * 2]

    def Right(self, i):
        return self.heap[i * 2 + 1]

    def display(self, msg='힙 트리'):
        print(msg, self.heap[1:])


    def insert(self, n):

        self.heap.append(n)  # 일단 제일 마지막에 삽입
        i = self.size()  # 이번에 삽입한 제일 막단의 위치
        while (i != 1 and n > self.parent(i)):
            self.heap[i] = self.parent(i)
            i = i // 2
        self.heap[i] = n


    def delete(self):

        parent = 2
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while child <= self.size():
                if self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child]: break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
        self.heap[parent] = last
        self.heap.pop(-1)
        return hroot


mx = MaxHip()
for i in range(5, 10):
    mx.insert(i)
mx.display()
mx.delete()
mx.display()
