class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size == 0

    def parent(self, i):
        return self.heap[i // 2]

    def Left(self, i):
        return self.heap[i * 2]

    def right(self, i):
        return self.heap[i * 2 + 1]

    def display(self, string="maxHeap"):
        print(string, self.heap[1:])  # 1번에는 0이 삽입되어 있으니까 이를 이용한다.

    def insert(self, data):
        self.heap.append(data)  # 제일 처음에 가장 작은 값이라고 가정하고 힙의 마지막에 삽임
        index = self.size()  # 삽입한 데이터 리스트의 인덱스를 반환
        while index != 1 and data > self.parent(index):  # 부모 노드 보다 새로 삽입한 data가 더 클때까지 반복
            self.heap[index] = self.parent(index)  # 부모가 더 작으니가 원래 부모를 끌어내린다.
            index = index // 2  # 인덱스를 부모노드의 인덱스로 다시 만들어서 더 위의 부모와 비교하기 위해서 수행한다.
        self.heap[index] = data  # 위 조건을 만족하는 index에 데이터를 삽입한다.

    def delete(self):

        parent = 1
        child = 2

        if not self.isEmpty():
            hroot = self.heap[1]  # 반환할 root최대값
            last = self.heap[self.size()]  # 교환을 위해서 마지막 노들르 저장함
            while child <= self.size():  # 마지막 인덱스 보다 작을 때까지 반복

                if self.size() > child and self.Left(parent) < self.right(parent):  # 부모 노드의 오른쪽 자식이 왼쪽 자식보다 크다면
                    child += 1  # 오른쪽 자식으로 바꾼다.
                if last >= self.heap[child]:  # 마지막 요소보다 작은 child를 찾았다면 last를 삽입할 위치를 찾음
                    break
                self.heap[parent] = self.heap[child]  # 부모 노드의 자리에 자식노드를 올림
                parent = child  # 부모를 자식으로 바꿈
                child = child * 2  # 자식을 한단계 밑으로 내린다.

            self.heap[parent] = last #마지막에 parent에 child가 삽입되고 끝났기 때문에 last를 parent의 위치에 삽입
            self.heap.pop(-1)# 삭제 연산은 결국 마지막 요소를 지우는 연산임
            return hroot#root를 반환
