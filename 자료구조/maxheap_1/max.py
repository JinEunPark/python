import random
class maxheap:
    def __init__(self):  # 배열 0번은 0으로 초기화
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def Parent(self, i):
        return self.heap[i // 2]

    def Left(self, i):
        return self.heap[i * 2]

    def Right(self, i):
        return self.heap[(i * 2) + 1]

    def display(self, msg='heap tree'):
        print(msg, self.heap[1:])

    def insert(self, node):
        self.heap.append(node)  # 일단 리스트 최하단에 넣어둬
        i = self.size()
        while i < self.size() and node > self.parent(i):  # 새로 들어온 노드가 부모노드 보다 클때까지
            self.heap[i] = self.parent(i)  # 부모가 밑으로 내려와
            i = i // 2  # 다음 부모 인덱스가 되게 만들어
        self.heap[i] = node  #

    def delete(self):

        rdata = self.heap[1]  # 일단 반환할 데이터 빼놔 진은아 1번은 트레쉬 값을 이용해서 0으로 초기화 했기때문에 사용하면 안된다.
        last = self.heap[self.size()]
        parent = 1
        child = 2

        while child < self.size():

            if child < self.size() and self.Left(parent) < self.Right(parent):
                child += 1
            if self.heap[child] <= last:
                break

            self.heap[parent] = self.heap[child]
            parent = child
            child = child*2

        self.heap[parent] = last
        self.heap.pop(-1) #맨 마지막 노삭제
        return rdata

m = maxheap()
for i in range(10):
    m.insert(int(random.random()*10))
m.display()
for i in range(3):
    m.delete()
m.display()
