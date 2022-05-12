class maxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)  # 배열의 첫번째 요소를 사용하지않는다.

    def size(self):
        return len(self.heap) - 1  # 첫번째 요소를 사용하지않게 만들기 위해서 -1을함

    def isEmpty(self):  # 첫번째 요소를 제외하고 길이를 반환하기 때문에 위에서 정의한 길이를 반환하는 함수가 0을 반환한다면 이를 힙이 빈것으로 간주한다,
        return self.size() == 0

    def parent(self, index):
        return self.heap[index // 2]  # 트리의 부모 인덱스는 자식 노드의 인데스 나누기 2를 하면되는데 이때 파이썬은 정수 나눗셈음 // 이다.

    # 조심할것
    def Left(self, parentIndex):
        return self.heap[parentIndex * 2]  # 왼쪽 자식의 인덱슨는 부모의 인덱스의 두배이다

    def Right(self, parentIndex):
        return self.heap[(parentIndex * 2) + 1]  # 오른쪽 자식의 인덱스는 부모의 인덱스의 두배 곱하기 2의 두배이다.

    def display(self, msg="heap tree"):
        print(msg, self.heap[1:])  # 제일 처음의 계산의 편리를 위해서 삽입한 0을 제외하고 출력하기 위해서 이를 제외하기 위해서

    # 파이선 함수의 슬라이싱을 이용해서 이를 바나환하엿다

    def insert(self, n):
        self.heap.append(n)  # 일단 새로 삽입할 정수를 리스트의 제일 하단에 붙인다.
        i = self.size()  # 리스트의 가장 끝단의 숫자를 반환해서 i를 제일 끝에 있는 수를 가리키게 만든다 아까 self.sizef()를 선언할 때 -1을 해주어서 사이즈를 반환하면 가장
        # 끝단 즉 리스트 끝에있는 요소의 인덱스가된다.
        while (i != 1 and n > self.parent(i)):  # i root가 아니고 새로들어온 정수인 n이 부모의 node보다 클때까지 반복한다.
            self.heap[i] = self.parent(i)  # i의 인덱스가 가리키는 힙 리스트에 부모리스트를 삽입한다.
            i = i // 2  # i를 나누기 2해서 부모의 인덱스를 가지게 만든다.
        self.heap[i] = n  # 마지막에 i가 부모인덱스를 가리게 되면 혹은 부모의 부모인덱스를 가리키게 되면 그 위치에 새로 들어온 정수를 삽입한다.

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():

            hroot = self.heap[1]  # 삭제하고 반환할 루트를 복사함
            last = self.heap[self.size()]
            # 마지막 노드 선택
            while (child <= self.size()):  # child라는 인덱스가 마지막 인덱스보다 작거나 같을때까지 반복
                # child 가 마지막 인덱스 보다작고 그리고 자신의 오른쪽 노드가 더 크면 child가 오른쪽 노드를 가르키게 만든다.
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child]:#마지막 요소보다 heap[child]가 작거나 같으면
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

ma = maxHeap()
data = [21,23, 42, 25, 234, 1]
for d in data:
    ma.insert(d)

ma.display()
ma.delete()
ma.display()
