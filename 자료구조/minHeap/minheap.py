class minheap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def display(self, msg="heap :"):
        print(msg, self.heap[1:])

    def parent(self, i):
        return self.heap[i // 2]

    def Left(self, parent):
        return self.heap[parent * 2]

    def Right(self, parent):
        return self.heap[(parent * 2) + 1]

    def insert(self, n):

        self.heap.append(n)
        i = self.size()

        while i != 1 and n < self.parent(i):  # maxheap이랑 다른 부분: 여기서 새로 반복문을 새로 들어온 정수가 부모의 정수보다 작을 때 까지 반복하는게 포인트
            # maxheap은 새로 들어온 정수가 부모 정수보다 클때가지만 반복문을 실행한다.
            self.heap[i] = self.parent(i)
            i = i // 2

        self.heap[i] = n

    def delete(self):

        child = 2
        parent = 1

        if not self.isEmpty():

            hroot = self.heap[1]  # 삭제하 노드를 미리복사
            last = self.heap[self.size()]  # 교환을 진행할 마지막 노드 미리 복사

            while child <= self.size():  # 자식 인덱스가 마지막 인덱스 보다 클때까지만 실행

                if child < self.size() and self.Left(parent) > self.Right(parent):
                    # 이것도 맥스 큐랑 다른 점인데 맥스 큐는 옆에 노드가 더 크다면 자식인덱스를 옆으로 옮겼지만
                    # 민힙에서는 가장 작은 자식이 root의 후보가 되기 때문에 이를 위해서 옆이 더 작으면 자삭노드로 옮긴다.
                    child += 1

                if last <= self.heap[child]:# 이것도 맥스 큐량 반대이다. 만약에 마지막 노드보다 작은 노드를 발견하면 바로 나간다.
                    break

                    self.heap[parent] = self.heap[child]
                    parent = child #부모를 같은 계층으로 만든다.
                    child *= 2#애를 더 아래 계층으로 내린다.

            self.heap[parent] = last#마지막에 부모인덱스랑 마지막 요소를 교환하고
            self.heap.pop(-1)#마지막 요소를 날려준다. 이미 위에서 부모 인덱스랑 교환해서 시발 가능하다.
            return hroot


min = minheap()
for i in range(0, 6):
    min.insert(i)
min.display()
for i in range(3):
    min.delete()
min.display()
